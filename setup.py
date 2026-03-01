import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'autonomous_navigation_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        # Include all config/yaml files
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))), 
        # Include map files (.yaml and .pgm)
        (os.path.join('share', package_name, 'maps'), glob(os.path.join('maps', '*'))),          
        # Include URDF/Xacro files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        # Include RViz configuration files
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        # Include Gazebo world files
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        # --- ADDED: Include Behavior Tree XML files ---
        (os.path.join('share', package_name, 'behavior_trees'), glob('behavior_trees/*.xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='salman',
    maintainer_email='msalman.mts44ceme@student.nust.edu.pk',
    description='Package for autonomous navigation research',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)