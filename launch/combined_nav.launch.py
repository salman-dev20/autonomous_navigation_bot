import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_path = get_package_share_directory('autonomous_navigation_bot')

    map_file_path = os.path.join(pkg_path, 'maps', 'my_test_maze.yaml')
    nav2_params_path = os.path.join(pkg_path, 'config', 'nav2_params.yaml')

    # 1. Robot & Gazebo Spawn
    launch_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(pkg_path, 'launch', 'rsp_spawn.launch.py')]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 2. RViz — starts immediately so it's ready to receive map
    run_rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'view_bot.rviz')],
        parameters=[{'use_sim_time': True}]
    )

    # 3. Map Server
    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'yaml_filename': map_file_path,
            'use_sim_time': True,
            'publish_period_sec': 2.0
        }]
    )

    # 4. AMCL
    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[nav2_params_path, {'use_sim_time': True}]
    )

    # 5. Planner Server
    planner_server = Node(
        package='nav2_planner',
        executable='planner_server',
        name='planner_server',
        output='screen',
        parameters=[nav2_params_path, {'use_sim_time': True}]
    )

    # 6. Controller Server
    controller_server = Node(
        package='nav2_controller',
        executable='controller_server',
        name='controller_server',
        output='screen',
        parameters=[nav2_params_path, {'use_sim_time': True}]
    )

    # 7. BT Navigator
    bt_navigator = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        name='bt_navigator',
        output='screen',
        parameters=[nav2_params_path, {'use_sim_time': True}]
    )

    # 8. Behaviors Server (Recoveries)
    recoveries_server = Node(
        package='nav2_behaviors',
        executable='behavior_server',
        name='recoveries_server',
        output='screen',
        parameters=[nav2_params_path, {'use_sim_time': True}]
    )

    # 9. Lifecycle Manager for Map
    lifecycle_manager_map = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_map',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'autostart': True,
            'bond_timeout': 0.0,
            'node_names': ['map_server']
        }]
    )

    # 10. Lifecycle Manager for Nav Stack
    lifecycle_manager_nav = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_nav',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'autostart': True,
            'bond_timeout': 0.0,
            'node_names': [
                'amcl',
                'planner_server',
                'controller_server',
                'recoveries_server',
                'bt_navigator'
            ]
        }]
    )

    # Return LaunchDescription with fixed indentation
    return LaunchDescription([
        # Start robot and RViz immediately
        launch_robot,
        run_rviz,

        # Start nav nodes after 3 seconds
        TimerAction(period=3.0, actions=[
            map_server_node,
            amcl_node,
            planner_server,
            controller_server,
            bt_navigator,
            recoveries_server,
        ]),

        # Activate map_server after 6 seconds
        TimerAction(period=6.0, actions=[
            lifecycle_manager_map,
        ]),

        # Activate nav stack after 9 seconds
        TimerAction(period=9.0, actions=[
            lifecycle_manager_nav,
        ]),
    ])