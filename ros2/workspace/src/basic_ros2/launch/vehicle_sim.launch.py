from pathlib import Path

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    package_share = Path(get_package_share_directory("basic_ros2"))
    urdf_path = package_share / "urdf" / "simple_vehicle.urdf"

    urdf_content = urdf_path.read_text()

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[{
                "robot_description": urdf_content
            }],
            output="screen"
        ),

        Node(
            package="ros_gz_sim",
            executable="create",
            arguments=[
                "-world", "vehicle_world",
                "-file", str(urdf_path),
                "-name", "simple_vehicle",
                "-x", "0",
                "-y", "0",
                "-z", "0"
            ],
            output="screen"
        ),

        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/camera/image@sensor_msgs/msg/Image@gz.msgs.Image",
                "/lidar/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan",
                "/imu/data@sensor_msgs/msg/Imu@gz.msgs.IMU"
            ],
            output="screen"
        )
    ])
