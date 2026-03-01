# 🤖 Autonomous Navigation Bot (ROS 2 Humble)

A fully integrated autonomous mobile robot simulation featuring a custom differential drive chassis, sensor fusion (LiDAR + Camera), and an optimized **Nav2** navigation stack for complex maze traversal.

## 📺 Project Demonstration
![Autonomous Navigation Demo](nav_demo.mp4)

---

## 🛠️ Technical Architecture

### 1. Robot Design (URDF)
- **Chassis:** 0.5m x 0.3m x 0.15m Differential Drive platform.
- **Sensors:** - **RP-LiDAR:** 360° Laser Scan for obstacle avoidance and AMCL localization.
  - **RGB Camera:** Front-mounted with a dedicated **Optical Link** transform ($z$-forward) to ensure correct image orientation in RViz.
- **Actuators:** Dual-wheel differential drive with a passive rear caster for high-maneuverability stability.



### 2. Navigation Stack (Nav2)
- **Localization:** AMCL (Adaptive Monte Carlo Localization) utilizing LiDAR data to estimate pose within a static map.
- **Brain:** Custom **Behavior Tree** (`simple_nav.xml`) managing goal execution, path planning, and real-time replanning.
- **Lifecycle Management:** Synchronized node activation (Map Server, AMCL, Planner, Controller) to ensure stable communication across the ROS 2 network.



---

## 📊 System Specifications & Tuning
| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Max Velocity** | 0.5 m/s | Optimized for maze stability |
| **Update Rate** | 20 Hz | Frequency of the Controller Server |
| **Inflation Radius** | 0.25m | Prevents wall collisions in tight turns |
| **LiDAR Range** | 12.0m | Maximum distance for obstacle detection |
| **Goal Tolerance** | 0.2m | Precision for reaching the target pose |

---

## 🚀 Build & Installation

### 1. Prerequisites
```bash
sudo apt update
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3-msgs
```

2. Setup & Build
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone [https://github.com/salman-dev20/autonomous_navigation_bot.git](https://github.com/salman-dev20/autonomous_navigation_bot.git)
cd ~/ros2_ws
colcon build --symlink-install --packages-select autonomous_navigation_bot
source install/setup.bash
```
🧭 How to Run
Launch Simulation: 
```bash
ros2 launch autonomous_navigation_bot combined_nav.launch.py

Localize: Use 2D Pose Estimate in RViz to align the robot.

Navigate: Use Nav2 Goal to set a destination.
```

📂 Project Structure
Plaintext
autonomous_navigation_bot/
├── behavior_trees/    # Custom XML navigation logic
├── config/            # Nav2 and AMCL parameters
├── launch/            # Combined Gazebo/Nav2 launch scripts
├── maps/              # Saved maze maps (.yaml, .pgm)
├── media/             # Demo videos and screenshots
├── urdf/              # Robot models and Gazebo plugins
└── README.md
