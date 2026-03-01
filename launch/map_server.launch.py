import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('autonomous_navigation_bot')
    map_file_path = os.path.join(pkg_path, 'maps', 'my_test_maze.yaml')

    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_file_path, 'use_sim_time': True, 'publish_period_sec': 2.0}]
    )

    # lifecycle_manager_node = Node(
    #     package='nav2_lifecycle_manager',
    #     executable='lifecycle_manager',
    #     name='lifecycle_manager_mapper',
    #     output='screen',
    #     parameters=[{
    #         'use_sim_time': True,
    #         'autostart': True,
    #         'node_names': ['map_server']
    #     }]
    # )

    return LaunchDescription([
        map_server_node,
        # lifecycle_manager_node
    ])