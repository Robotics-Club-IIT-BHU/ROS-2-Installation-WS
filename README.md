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

💡 **Pro Tip:** Dual boot = 😎 for real robotics work!  
⚠️ **Warning:** Backup your data before dual booting!
## ⚡ Quick Installation of ROS2
 **ROS 2 Humble Hawksbill (Installation Guide)**:
   - [Installation Guide for ROS 2](https://docs.ros.org/en/humble/Installation.html)

#### Installation Steps{just copy and paste each command in terminal [for pasting commands in the terminal, press ctrl+shift+v]}

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
#### 6. Check Installation:
##### Open terminal 1:
```bash
ros2 run demo_nodes_cpp talker
```
##### Open terminal 2:
```bash
ros2 run demo_nodes_py listener
```
 
