#!/usr/bin/python3

import rclpy
from rclpy.node import Node
import threading
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy, Imu

class Segway_controller(Node):

    def __init__(self):
        super().__init__('segway_controller')

        self.pitch_angle = 0
        self.integral_pitch_error = 0
        self.last_error_pitch = 0

        self.vel_msg = Twist()

        self.Kp_y = 28
        self.Ki_y = 20
        self.Kd_y = 180

        self.time_interval = 0.005

        self.publisher_ = self.create_publisher(Twist, '/segway/cmd_vel', 10)
        self.timer = self.create_timer(self.time_interval, self.timer_callback)

    def timer_callback(self):

        error_pitch  = joy_subscriber.target_pitch_angle - imu_subscriber.pitch
        self.integral_pitch_error += (error_pitch + self.last_error_pitch)*self.time_interval/2
        vel = (self.Kp_y*error_pitch  + 
                      self.Ki_y*self.integral_pitch_error +
                      self.Kd_y*(error_pitch - self.last_error_pitch)/self.time_interval)
 
        self.last_error_pitch = error_pitch
        self.vel_msg.linear.x = vel
        self.vel_msg.angular.z = float(joy_subscriber.target_w)
        self.publisher_.publish(self.vel_msg)

class IMU_subscriber(Node):

    def __init__(self):
        super().__init__('imu_subscriber')
        self.pitch = 0
        self.subscription = self.create_subscription(
            Imu,
            '/imu_plugin/out',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, data):
        q0 = data.orientation.x
        q1 = data.orientation.y
        q2 = data.orientation.z
        q3 = data.orientation.w

        self.pitch = math.asin(2*(q0*q2 - q1*q3)) 

class Joy_subscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')
        self.target_pitch_angle = 0
        self.target_w = 0
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, data):
        self.target_pitch_angle = -data.axes[1]/50
        self.target_w = -data.axes[0]*2  

if __name__ == '__main__':

    rclpy.init(args=None)
    
    segway_controller = Segway_controller()
    imu_subscriber = IMU_subscriber()
    joy_subscriber = Joy_subscriber()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(segway_controller)
    executor.add_node(imu_subscriber)
    executor.add_node(joy_subscriber)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()

    rate = segway_controller.create_rate(2)
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
    executor_thread.join()
