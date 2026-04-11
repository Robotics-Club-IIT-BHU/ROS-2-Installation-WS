# 🚀 ROS 2 Installation Workshop

[![ROS 2](https://img.shields.io/badge/ROS-2-%230A0FF9)](https://docs.ros.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

The ultimate guide to setting up your ROS 2 development environment with awesome simulations!

## Welcome Robotics Enthusiasts!

This repository will help you:

- Dual Boot your System.
- Install ROS 2 quickly and painlessly
- Get access to some cool pre-configured simulations
- Jumpstart your robotics projects

## 🛠️ System Requirements

- Ubuntu 22.04 (Jammy)
- At least 4GB RAM (8GB recommended for simulations)
- 50GB+ free disk space
- Stable internet connection

## DUAL BOOT or VM BOX Installation

Choose your adventure:

### Option 1: **Dual Boot (Windows)**
🔹 Better performance (full hardware access)  
🔹 Recommended for serious ROS development  
   [Complete Dual Boot Guide](https://docs.google.com/document/d/1RVChwuKGptD5uSHYs5tflR0sVBAdXiwsjumxEQVBVG4/edit?usp=sharing)  

   **Most of you need to install only** [LINK](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-desktop-amd64.iso)
   this One - **64-bit PC (AMD64) desktop image**

### Option 2: **Virtual Machine (Windows/Mac)**
🔹 Safer for beginners (no partitioning)  
🔹 Easy to delete if something goes wrong  
[VM Setup Guide](https://docs.google.com/document/d/1L55AWdZwC15YzvmSWa1djZLB4AHl80aEcOfpS0ie9nM/edit?usp=sharing)  

  **For Mac M1/M2, you need to install only** [LINK](https://cdimage.ubuntu.com/releases/22.04/release/)
  this one - **64-bit ARM (ARMv8/AArch64) server install image**

**Pro Tip:** Dual boot = for real robotics work!  
**Warning:** Backup your data before dual booting!
## Quick Installation of ROS2
 **ROS 2 Humble Hawksbill (Installation Guide)**:
   - [Installation Guide for ROS 2](https://docs.ros.org/en/humble/Installation.html)

## Installation Steps{just copy and paste each command in terminal [for pasting commands in the terminal, press ctrl+shift+v]}

# For Ubuntu (Dual-boot or VM)

#### 1. Open Terminal in Ubuntu & Set Locale:
```bash
locale  # check for UTF-8
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
locale  # verify settings
```
#### 2. Setup Sources:
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```
#### Add ROS 2 GPG key with apt:
```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
#### Add the ROS 2 repository:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
#### 3. Install ROS 2 packages:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ros-humble-desktop
```
#### 4. Install Gazebo Harmonic for ROS 2:
```bash
sudo wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt update
sudo apt install gz-harmonic
```
#### 5. Environment Setup:
```bash
source /opt/ros/humble/setup.bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## ROS 2 - Gazebo Integration
### Install Integration Packages
```bash
sudo apt update
sudo apt install -y ros-humble-ros-gzharmonic
```
```bash
echo "export GZ_VERSION=harmonic" >> ~/.bashrc
source ~/.bashrc
```
### Open the terminal and write the following cmd:-
```bash
sudo apt install python3-colcon-common-extensions
```
### Create and build a Workspace
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```
### Source the Workspace
```bash
echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
```


# Installation Guide for ROS 2 Humble and Gazebo Harmonic on Ubuntu 22.04 (ARM)

This guide provides step-by-step instructions to install ROS 2 Humble and Gazebo Harmonic on an ARM-based Ubuntu 22.04 system, including environment setup and optimizations for ARM architecture.

**Initial System Setup**
   ```bash
   # Update system
   sudo apt update
   sudo apt upgrade -y
   
   # Install required dependencies
   sudo apt install -y software-properties-common build-essential cmake git curl wget gnupg lsb-release
  ```


## 1. ROS 2 Humble Installation

### Set Locale
```bash
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```
### Add ROS 2 Repository
```bash
sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Install ROS 2 Humble
```bash
sudo apt update
sudo apt install -y ros-humble-desktop
```
### Setup ROS 2 Environment
```bash
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc
```
### Install Development Tools
```bash
sudo apt install -y ros-dev-tools python3-colcon-common-extensions python3-rosdep python3-pip
sudo rosdep init
rosdep update
```

## 2. Gazebo Harmonic Installation
### Add Gazebo Repository
```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
```
### Install Gazebo Harmonic
```bash
sudo apt update
sudo apt install -y gz-harmonic
```
### Environment Setup for ARM
```bash
echo 'export LIBGL_ALWAYS_SOFTWARE=1' >> ~/.bashrc
echo 'export MESA_GL_VERSION_OVERRIDE=3.3' >> ~/.bashrc
echo 'export OGRE_RTT_MODE=Copy' >> ~/.bashrc
source ~/.bashrc
```

## 3. ROS 2 - Gazebo Integration
### Install Integration Packages
```bash
sudo apt update
sudo apt install -y ros-humble-ros-gz-bridge ros-humble-ros-gz-sim ros-humble-ros-gz-interfaces
```
### Create a Workspace
```bash
mkdir -p ~/ros_gz_ws/src
cd ~/ros_gz_ws/src
```

### Clone Integration Packages 
```bash
# Environment variables to optimize compilation on ARM
export ASAN_OPTIONS=detect_leaks=0
export CCACHE_SLOPPINESS=pch_defines,time_macros
export CCACHE_COMPRESS=1
export CCACHE_MAXSIZE=5G

# Build with single thread to avoid memory issues
MAKEFLAGS="-j1" colcon build --symlink-install --packages-select ros_gz_bridge --cmake-args -DCMAKE_CXX_FLAGS="-O1"

# Build other packages
colcon build --symlink-install --packages-skip ros_gz_bridge
```
### Source the Workspace
```bash
echo 'source ~/ros_gz_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
```
### Open the terminal and write the following cmd:-
```bash
sudo apt install python3-colcon-common-extensions
```
# Check Installation:
##### Open terminal 1:
```bash
ros2 run demo_nodes_cpp talker
```
##### Open terminal 2:
```bash
ros2 run demo_nodes_py listener
```


# 🚀 ROS 2 Humble & Gazebo Harmonic Installation (Mac ARM / Apple Silicon)

This guide provides step-by-step instructions to install **ROS 2 Humble** and **Gazebo Harmonic** on M1/M2/M3 Macs using virtualization. 

⚠️ **CRITICAL ARCHITECTURE WARNING:** ROS 2 Humble requires **Ubuntu 22.04 LTS**. Do not use Ubuntu 24.04. Furthermore, you must use the **ARM64** version of Ubuntu, not the AMD64 desktop version. 
---
## Part 1: System & UTM Virtual Machine Setup

1. **Download UTM:** Get the virtual machine software from [mac.getutm.app](https://mac.getutm.app/). (https://www.youtube.com/watch?v=nUhQy5PDj2A&t=1129s)
2. **Download Ubuntu 22.04 ARM Server:** Download the `Ubuntu 22.04 LTS ARM64 Server` ISO from the alternative architectures page on the official Ubuntu website.
3. **Configure UTM:**
   * Open UTM and click **+** -> **Virtualize** -> **Linux**.
   * Browse and select the Ubuntu 22.04 ARM Server ISO.
   * **RAM:** Allocate at least `4096 MB` (8GB recommended).
   * **CPU:** Allocate 4 to 8 cores.
   * **Storage:** Allocate at least **64 GB** (ROS 2 and Gazebo take up significant space).
4. **Install Ubuntu Server:**
   * Boot the VM and follow the standard "Try or Install Ubuntu Server" prompts.
   * *Troubleshooting Note:* If the VM hangs on the reboot log after installation finishes, power off the VM, click the CD/DVD dropdown in the UTM settings, select **Clear** to remove the ISO, and start it again.
5. **Install Graphical Interface (GUI):**
   * Log into the command line and run:
     ```bash
     sudo apt update
     sudo apt install tasksel
     sudo apt install ubuntu-desktop
     ```
   * *This will take 20-30 minutes.* Once complete, run `sudo reboot now`.
6. **Enable Retina Resolution & Copy/Paste:**
   * Log into your new desktop environment, open the terminal, and install the SPICE tools:
     ```bash
     sudo apt install spice-vdagent spice-webdavd
     ```
   * Shut down the VM. In UTM Settings -> Display, check **Retina Mode**. Start the VM again.

---

## Part 2: ROS 2 Humble Installation

Open the terminal in your Ubuntu VM and run the following commands sequentially.

### 1. Initial System Setup
```bash
# Update system and install required dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y software-properties-common build-essential cmake git curl wget gnupg lsb-release locales

# Set Locale
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Add ROS 2 GPG Key and Repository
wget -qO- https://packages.osrfoundation.org/gazebo.gpg | sudo tee /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
git clone https://github.com/gazebosim/ros_gz.git -b humble

# Install ROS 2 Humble Desktop
sudo apt update
sudo apt install -y ros-humble-desktop

# Setup Environment
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc

# Install Dev Tools & Initialize rosdep
sudo apt install -y ros-dev-tools python3-colcon-common-extensions python3-rosdep python3-pip
sudo rosdep init || true
rosdep update

# Add Gazebo Repository
wget -qO- [https://packages.osrfoundation.org/gazebo.gpg](https://packages.osrfoundation.org/gazebo.gpg) | sudo tee /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] [http://packages.osrfoundation.org/gazebo/ubuntu-stable](http://packages.osrfoundation.org/gazebo/ubuntu-stable) $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

# Install Gazebo Harmonic
sudo apt update
sudo apt install -y gz-harmonic

# Optimize VM Graphics for ARM MacBooks
echo 'export LIBGL_ALWAYS_SOFTWARE=1' >> ~/.bashrc
echo 'export MESA_GL_VERSION_OVERRIDE=3.3' >> ~/.bashrc
echo 'export OGRE_RTT_MODE=Copy' >> ~/.bashrc
source ~/.bashrc

# Create the workspace
mkdir -p ~/ros_gz_ws/src
cd ~/ros_gz_ws/src

# Clone the proper humble branch for the integration packages
git clone [https://github.com/gazebosim/ros_gz.git](https://github.com/gazebosim/ros_gz.git) -b humble

cd ~/ros_gz_ws

# CRITICAL: Tell the compiler to target Harmonic instead of Fortress
export GZ_VERSION=harmonic

# Set environment variables to prevent the VM from running out of RAM during compilation
export ASAN_OPTIONS=detect_leaks=0
export CCACHE_SLOPPINESS=pch_defines,time_macros
export CCACHE_COMPRESS=1
export CCACHE_MAXSIZE=5G

# Install ROS dependencies for the workspace
rosdep install -r --from-paths src -i -y --rosdistro humble

# Build the workspace (using a single thread to avoid VM freezing/crashing)
MAKEFLAGS="-j1" colcon build --symlink-install --cmake-args -DCMAKE_CXX_FLAGS="-O1"

# Source the newly built bridge
echo 'source ~/ros_gz_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

# For demo in terminal one open this 
```bash
ros2 run demo_nodes_cpp talker
```
# And in second terminal run this command
```bash
ros2 run demo_nodes_py listener
```


## Some simulations

### 1. Turtlesim (Built-in ROS 2 Simulator)

Turtlesim is a lightweight 2D simulator built into ROS 2. It's the easiest way to verify your installation and learn core ROS 2 concepts like nodes, topics, and services.

#### Launch Turtlesim:
```bash
ros2 run turtlesim turtlesim_node
```

#### Control the Turtle (open a new terminal):
```bash
ros2 run turtlesim turtle_teleop_key
```
Use arrow keys to move the turtle around the window.

#### Draw a circle (open another terminal):
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0}, angular: {z: 1.8}}"
```

#### View active nodes and topics:
```bash
#in different terminals
ros2 node list
ros2 topic list
```
You will learn more about these terms in depth soon.

---

### 2. Differential Drive Robot in Gazebo Harmonic

A built-in Gazebo demo of a two-wheeled differential drive robot. No extra packages needed.

#### Launch the simulation:
```bash
gz sim diff_drive.sdf
```

This opens a Gazebo Harmonic window with a two-wheeled robot ready to drive.

#### Drive the robot forward (open a new terminal):
```bash
gz topic -t "/model/vehicle_blue/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 1.0}"
```

#### Turn the robot:
```bash
gz topic -t "/model/vehicle_blue/cmd_vel" -m gz.msgs.Twist -p "angular: {z: 0.5}"
```

#### Drive and turn together:
```bash
gz topic -t "/model/vehicle_blue/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 1.0}, angular: {z: 0.5}"
```
> **Note:** Make sure to play the simulation by clicking the play button on the bottom left in Gazebo.

#### View active Gazebo topics:
```bash
gz topic -l
```

> **Note:** On Mac, make sure Gazebo Harmonic is installed before running these commands.

---


### Phew, you made it to the end! Thanks for hangin' in there like a champ
