import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('autonomous_navigation_bot')

    # 1. Spawn Robot & Gazebo
    launch_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(pkg_path, 'launch', 'rsp_spawn.launch.py')]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 2. Load the Saved Map
    launch_map_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(pkg_path, 'launch', 'map_server.launch.py')])
    )

    # 3. Localization (AMCL)
    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'base_frame_id': "base_link",
            'odom_frame_id': "odom",
            'scan_topic': '/scan'
        }]
    )

    # 4. Lifecycle Manager (Crucial for activating Map & AMCL)
    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_nav',
        output='screen',
        parameters=[{'use_sim_time': True,
                     'autostart': True,
                     'node_names': ['map_server', 'amcl']}]
    )

    # 5. RViz with your custom config
    run_rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'view_bot.rviz')],
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        launch_robot,
        launch_map_server,
        amcl_node,
        lifecycle_manager,
        run_rviz
    ])
