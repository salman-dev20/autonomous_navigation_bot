import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg = get_package_share_directory('autonomous_navigation_bot')
    
    # 1. World Path
    world_path = os.path.join(pkg, 'worlds', 'my_test_world.world')

    # 2. Path to URDF - Using 'urdf' folder to match your setup.py
    urdf_path = os.path.join(pkg, 'urdf', 'robot.urdf')
    
    with open(urdf_path, 'r') as f: 
        robot_desc = f.read()

    # 3. Nodes - All indented exactly 4 spaces
    rsp = Node(
        package='robot_state_publisher', 
        executable='robot_state_publisher', 
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )
    
    jsp = Node(
        package='joint_state_publisher', 
        executable='joint_state_publisher', 
        parameters=[{'use_sim_time': True}]
    )
    
    # 4. Gazebo - This is line 29 area
    gz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world_path}.items()
    )

    sp = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py', 
        arguments=['-topic', 'robot_description', '-entity', 'nav_bot'], 
        output='screen'
    )

    return LaunchDescription([rsp, jsp, gz, sp])