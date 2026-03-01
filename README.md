# 🤖 Autonomous Navigation Bot (ROS 2 Humble)

A fully integrated autonomous mobile robot simulation featuring a custom differential drive chassis, sensor fusion (LiDAR + Camera), and an optimized **Nav2** navigation stack for complex maze traversal.

## 📺 Project Demonstration
![Autonomous Navigation Demo](media/nav_demo.mp4)
*(Note: If the video does not play, ensure it is uploaded to the 'media' folder in this repository)*

---

## 🛠️ Technical Architecture

### 1. Robot Design (URDF)
- **Chassis:** 0.5m x 0.3m x 0.15m Differential Drive platform.
- **Sensors:** - **RP-LiDAR:** 360° Laser Scan for obstacle avoidance and AMCL localization.
  - **RGB Camera:** Front-mounted with a dedicated **Optical Link** transform to ensure correct image orientation in RViz.
- **Actuators:** Dual-wheel differential drive with a passive rear caster for high-maneuverability stability.

[Image of ROS 2 camera coordinate frames showing standard vs optical rotation]

### 2. Navigation Stack (Nav2)
- **Localization:** AMCL (Adaptive Monte Carlo Localization) utilizing LiDAR data to estimate pose within a static map.
- **Brain:** Custom **Behavior Tree** (`simple_nav.xml`) managing goal execution, path planning, and real-time replanning.
- **Lifecycle Management:** Synchronized node activation (Map Server, AMCL, Planner, Controller) to ensure stable communication across the ROS 2 network.

[Image of ROS 2 Nav2 navigation stack block diagram showing Planner, Controller, and Behavior Tree connections]

---

## 🚀 Build & Installation

Follow these steps to set up the workspace and build the navigation package on your local machine.

### 1. Prerequisites
- **OS:** Ubuntu 22.04 (or WSL2)
- **Distribution:** ROS 2 Humble & Gazebo Classic
- **Required Packages:**
```bash
sudo apt update
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3-msgs
