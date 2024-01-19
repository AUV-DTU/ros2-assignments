import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Int32 

class randompublisher(Node):

    def __init__(self):
        super().__init__('random_publisher')
        self.publisher_ = self.create_publisher(Int32, 'topic_number', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self) :
        msg = Int32()
        msg.data = random.randint(1,100)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
 
 
def main(args=None):
    rclpy.init(args=args)

    random_publisher = randompublisher()

    rclpy.spin(random_publisher)

    random_publisher.destroy_node()
    rclpy.shutdown()
