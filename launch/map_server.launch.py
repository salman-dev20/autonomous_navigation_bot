import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('autonomous_navigation_bot')
    map_file_path = os.path.join(pkg_path, 'maps', 'my_test_maze.yaml')

    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',  # This name MUST match your Master file list
            output='screen',
            parameters=[{'yaml_filename': map_file_path, 'use_sim_time': True}]
        )
    ])