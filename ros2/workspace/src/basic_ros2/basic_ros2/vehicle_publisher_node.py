# vehicle_publisher_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class VehiclePublisher(Node):

    def __init__(self):
        super().__init__('vehicle_publisher')

        self.speed_publisher = self.create_publisher(
            Float32, '/vehicle_speed', 10
        )

        self.steering_publisher = self.create_publisher(
            Float32, '/vehicle_steering', 10
        )

        self.timer = self.create_timer(1.0, self.publish_vehicle_data)
        self.speed = 2.0
        self.steering = 0.1

    def publish_vehicle_data(self):
        speed_msg = Float32()
        speed_msg.data = self.speed
        self.speed_publisher.publish(speed_msg)

        steering_msg = Float32()
        steering_msg.data = self.steering
        self.steering_publisher.publish(steering_msg)

        self.get_logger().info(
            f'Speed: {self.speed:.2f} m/s | '
            f'Steering: {self.steering:.2f} rad'
        )


def main(args=None):
    rclpy.init(args=args)
    node = VehiclePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()