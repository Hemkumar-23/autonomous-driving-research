# 2-20D — Basic ROS 2 Subscriber Node

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BasicSubscriber(Node):

    def __init__(self):
        super().__init__('basic_subscriber')

        self.subscription = self.create_subscription(
            String,
            'basic_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, message):
        self.get_logger().info(
            f'Received: {message.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = BasicSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
