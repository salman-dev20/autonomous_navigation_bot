import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'autonomous_navigation_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
# Inside setup.py
# Inside ~/ros2_ws/src/autonomous_navigation_bot/setup.py
data_files=[
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
  (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))), 
    (os.path.join('share', package_name, 'maps'), glob(os.path.join('maps', '*'))),          
    (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
(os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
    # Use *.world to avoid copying hidden system folders that crash the build
    (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
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