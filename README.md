# 🚀 ROS 2 Installation Workshop

[![ROS 2](https://img.shields.io/badge/ROS-2-%230A0FF9)](https://docs.ros.org)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

🤖 The ultimate guide to setting up your ROS 2 development environment with awesome simulations! 🌟

## 🌈 Welcome Robotics Enthusiasts!

Future robotics pioneers, welcome! This repository will help you:

- Dual Boot your System.
- Install ROS 2 quickly and painlessly
- Get access to cool pre-configured simulations
- Jumpstart your robotics projects

## 🛠️ System Requirements

- Ubuntu 22.04 (Jammy)
- At least 4GB RAM (8GB recommended for simulations)
- 15GB+ free disk space
- Stable internet connection

## ⚡ DUAL BOOT or VM BOX Installation  🖥️🔀🐧

Choose your adventure:

### Option 1: 🖥️➡️🐧 **Dual Boot (Windows)**
🔹 Better performance (full hardware access)  
🔹 Recommended for serious ROS development  
📌 [Complete Dual Boot Guide](https://docs.google.com/document/d/1RVChwuKGptD5uSHYs5tflR0sVBAdXiwsjumxEQVBVG4/edit?usp=sharing)  

### Option 2: 🖥️📦 **Virtual Machine (Windows/Mac)**
🔹 Safer for beginners (no partitioning)  
🔹 Easy to delete if something goes wrong  
📌 [VM Setup Guide](https://docs.google.com/document/d/1L55AWdZwC15YzvmSWa1djZLB4AHl80aEcOfpS0ie9nM/edit?usp=sharing)  

  **Ubuntu 22.04 you need to install only**. [LINK](https://cdimage.ubuntu.com/releases/22.04/release/)
  This One - **64-bit ARM (ARMv8/AArch64) server install image**

💡 **Pro Tip:** Dual boot = 😎 for real robotics work!  
⚠️ **Warning:** Backup your data before dual booting!
## ⚡ Quick Installation of ROS2
 **ROS 2 Humble Hawksbill (Installation Guide)**:
   - [Installation Guide for ROS 2](https://docs.ros.org/en/humble/Installation.html)

## Installation Steps{just copy and paste each command in terminal [for pasting commands in the terminal, press ctrl+shift+v]}

# For Windows

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
sudo apt upgrade
sudo apt install ros-humble-desktop
```
#### 4. Install Gazebo for ROS 2:
```bash
sudo apt install ros-humble-gazebo-ros
```
#### 5. Environment Setup:
```bash
source /opt/ros/humble/setup.bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
# For Mac User:

**Initial System Setup**
   ```bash
   # Update system
   sudo apt update
   sudo apt upgrade -y
   
   # Install required dependencies
   sudo apt install -y software-properties-common build-essential cmake git curl wget gnupg lsb-release
  ```

# Installation Guide for ROS 2 Humble and Gazebo Harmonic on Ubuntu 22.04 (ARM)

This guide provides step-by-step instructions to install ROS 2 Humble and Gazebo Harmonic on an ARM-based Ubuntu 22.04 system, including environment setup and optimizations for ARM architecture.

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

# Check Installation:
##### Open terminal 1:
```bash
ros2 run demo_nodes_cpp talker
```
##### Open terminal 2:
```bash
ros2 run demo_nodes_py listener
```

# 🌈 Welcome to the simulation!
Download the given package if all the above process are done.
Open the terminal and write the following cmd:-
```bash
sudo apt install python3-colcon-common-extensions
```
### MOVE the models folder to the gazebo models folder then 
```bash
cd segway_Humble
colcon build
```
for launching the simulation first source the WS 
```bash
source install/setup.bash
```
 ```bash
ros2 launch segway_gazebo segway_sim.launch.py 
```
 this will launch the simulation 
 for controlling the bot open new terminal and type 
  ```bash
python3 segway_control1.py 
```
 then use the W A S D to navigate and X to stop

### Phew, you made it to the end! 😮‍💨🎉 Thanks for hangin' in there like a champ 💪😄 Now go rest those eyeballs 👀🛌😂
