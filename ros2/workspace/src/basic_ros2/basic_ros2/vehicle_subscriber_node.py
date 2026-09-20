# vehicle_subscriber_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class VehicleSubscriber(Node):

    def __init__(self):
        super().__init__('vehicle_subscriber')

        self.speed_subscription = self.create_subscription(
            Float32,
            '/vehicle_speed',
            self.speed_callback,
            10
        )

        self.steering_subscription = self.create_subscription(
            Float32,
            '/vehicle_steering',
            self.steering_callback,
            10
        )

    def speed_callback(self, message):
        self.get_logger().info(
            f'Received speed: {message.data:.2f} m/s'
        )

    def steering_callback(self, message):
        self.get_logger().info(
            f'Received steering: {message.data:.2f} rad'
        )


def main(args=None):
    rclpy.init(args=args)
    node = VehicleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()