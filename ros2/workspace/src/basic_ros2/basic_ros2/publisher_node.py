# 1-20D — Basic ROS 2 Publisher Node

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BasicPublisher(Node):

    def __init__(self):
        super().__init__('basic_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'basic_topic',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

        self.counter = 0

    def publish_message(self):
        message = String()
        message.data = f'Hello ROS 2: {self.counter}'

        self.publisher_.publish(message)

        self.get_logger().info(
            f'Publishing: {message.data}'
        )

        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = BasicPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
