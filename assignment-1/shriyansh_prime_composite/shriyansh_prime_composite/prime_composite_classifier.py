import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int32


def isprime(a) :
    for i in range (2,a) :
        if a%i == 0 :
            return(True)
            break

    
class primeclassifier(Node):

    def __init__(self):
        super().__init__('prime_classifier')
        self.subscription = self.create_subscription(
            Int32,
            'topic_number',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        if isprime(msg.data) :
            a = ("composite number",msg.data)
        else :
            a = ("prime number",msg.data)
        
        self.get_logger().info('answer is : "%s","%d"' % a)
       
def main(args=None):
    rclpy.init(args=args)

    prime_classifier = primeclassifier()

    rclpy.spin(prime_classifier)


    prime_classifier.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

