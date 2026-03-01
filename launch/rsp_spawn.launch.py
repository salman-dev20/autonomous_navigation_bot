import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    pkg = get_package_share_directory('autonomous_navigation_bot')
    
    world_path = os.path.join(pkg, 'worlds', 'my_test_world.world')
    urdf_path = os.path.join(pkg, 'urdf', 'robot.urdf')
    
    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

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

    # Launch gzserver and gzclient directly instead of using gazebo.launch.py
    gzserver = ExecuteProcess(
        cmd=['gzserver', '--verbose', world_path, '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    gzclient = ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    sp = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'nav_bot'],
        output='screen'
    )

    return LaunchDescription([rsp, jsp, gzserver, gzclient, sp])