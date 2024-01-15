import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RandomSubscriber(Node):

    def __init__(self):
        super().__init__('random_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic_numbers',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        num = int(msg.data)
        if num > 1:
            for i in range(2, num):
            	if num % i == 0:
            	    self.get_logger().info('"%s" is COMPOSITE' % msg.data)
            	    break
            else:
            	self.get_logger().info('"%s" is PRIME' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    random_subscriber = RandomSubscriber()

    rclpy.spin(random_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    random_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
