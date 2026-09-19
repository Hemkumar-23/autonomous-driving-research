from setuptools import find_packages, setup

package_name = 'basic_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hemkumar',
    maintainer_email='shemkumar23@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = basic_ros2.publisher_node:main',
            'subscriber = basic_ros2.subscriber_node:main',
            'vehicle_publisher = basic_ros2.vehicle_publisher_node:main',
            'vehicle_subscriber = basic_ros2.vehicle_subscriber_node:main',
        ],
    },
)
