import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan


class AutonomousVehicle(Node):

    def __init__(self):
        super().__init__('autonomous_vehicle')

        self.speed = 0.0
        self.steering = 0.0
        self.obstacle_distance = float('inf')

        self.speed_publisher = self.create_publisher(
            Float32,
            '/vehicle_speed',
            10
        )

        self.steering_publisher = self.create_publisher(
            Float32,
            '/vehicle_steering',
            10
        )

        self.lidar_subscription = self.create_subscription(
            LaserScan,
            '/lidar/scan',
            self.lidar_callback,
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.get_logger().info(
            'Autonomous vehicle node started.'
        )

    def lidar_callback(self, message):
        valid_ranges = [
            distance for distance in message.ranges
            if message.range_min <= distance <= message.range_max
        ]

        if valid_ranges:
            self.obstacle_distance = min(valid_ranges)

    def control_loop(self):
        if self.obstacle_distance < 3.0:
            self.speed = 0.0
            self.steering = 0.0
        else:
            self.speed = 2.0
            self.steering = 0.0

        speed_msg = Float32()
        speed_msg.data = self.speed
        self.speed_publisher.publish(speed_msg)

        steering_msg = Float32()
        steering_msg.data = self.steering
        self.steering_publisher.publish(steering_msg)

        self.get_logger().info(
            f'Obstacle: {self.obstacle_distance:.2f} m | '
            f'Speed: {self.speed:.2f} m/s | '
            f'Steering: {self.steering:.2f} rad'
        )


def main(args=None):
    rclpy.init(args=args)

    node = AutonomousVehicle()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
