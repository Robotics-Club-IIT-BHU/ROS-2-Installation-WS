#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
import math
import threading
import sys
import select
import termios
import tty

class IMU_subscriber(Node):

    def __init__(self):
        super().__init__('imu_subscriber')
        self.pitch = 0.0
        self.subscription = self.create_subscription(
            Imu,
            '/imu_plugin/out',
            self.listener_callback,
            10)

    def listener_callback(self, data):
        q0 = data.orientation.x
        q1 = data.orientation.y
        q2 = data.orientation.z
        q3 = data.orientation.w
        try:
            self.pitch = math.asin(2 * (q0 * q2 - q1 * q3))
        except:
            self.pitch = 0.0


class Segway_controller(Node):

    def __init__(self, imu, keyboard):
        super().__init__('segway_controller')

        self.imu = imu
        self.keyboard = keyboard

        self.pitch_angle = 0.0
        self.integral_pitch_error = 0.0
        self.last_error_pitch = 0.0

        self.Kp_y = 28
        self.Ki_y = 20
        self.Kd_y = 180

        self.publisher_ = self.create_publisher(Twist, '/segway/cmd_vel', 10)
        self.timer = self.create_timer(0.01, self.timer_callback)

    def timer_callback(self):
        error_pitch = self.keyboard.target_pitch_angle - self.imu.pitch
        self.integral_pitch_error += (error_pitch + self.last_error_pitch) * 0.01 / 2
        vel = (self.Kp_y * error_pitch +
               self.Ki_y * self.integral_pitch_error +
               self.Kd_y * (error_pitch - self.last_error_pitch) / 0.01)

        self.last_error_pitch = error_pitch

        msg = Twist()
        msg.linear.x = vel
        msg.angular.z = float(self.keyboard.target_w)
        self.publisher_.publish(msg)

class KeyboardControl:
    def __init__(self):
        self.target_pitch_angle = 0.0
        self.target_w = 0.0

        self.settings = termios.tcgetattr(sys.stdin)
        self.key_bindings = {
            'w': (0.2, 0.0),
            's': (-0.2, 0.0),
            'a': (0.0, 0.3),
            'd': (0.0, -0.3),
            'x': (0.0, 0.0)
        }

        self.thread = threading.Thread(target=self.key_loop, daemon=True)
        self.thread.start()

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def key_loop(self):
        print("\nControl Bot with W A S D. Press 'X' to stop.\n")
        while True:
            key = self.get_key()
            if key in self.key_bindings:
                self.target_pitch_angle, self.target_w = self.key_bindings[key]
                print(f"Pressed {key} → pitch: {self.target_pitch_angle:.3f}, turn: {self.target_w:.2f}")
            elif key == '\x03':
                break


def main(args=None):
    rclpy.init(args=args)

    imu_sub = IMU_subscriber()
    keyboard_input = KeyboardControl()
    segway_ctrl = Segway_controller(imu_sub, keyboard_input)

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(imu_sub)
    executor.add_node(segway_ctrl)

    try:
        executor.spin()
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
