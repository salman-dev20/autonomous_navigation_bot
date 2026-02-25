import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Ensure all lines below are indented 4 spaces
    pkg_path = get_package_share_directory('autonomous_navigation_bot')
    
    # This was the line causing the IndentationError
    slam_params_path = os.path.join(pkg_path, 'config', 'my_slam_params.yaml')

    # 1. Spawn Robot & Gazebo
    launch_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(pkg_path, 'launch', 'rsp_spawn.launch.py')]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 2. SLAM Toolbox
    launch_slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')
        ]),
        # Added the params file argument here so your config actually loads
        launch_arguments={
            'use_sim_time': 'true',
            'slam_params_file': slam_params_path
        }.items()
    )

    # 3. RViz
    run_rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'view_bot.rviz')],
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        launch_robot,
        launch_slam,
        run_rviz
    ])