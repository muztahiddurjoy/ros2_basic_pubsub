import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ROBUSubscriber(Node):
    def __init__(self):
        super().__init__('robu_subscriber')
        self.subscription = self.create_subscription(String,'robu_topic',self.receive_message,10)
    
    def receive_message(self,msg):
        self.get_logger().info(f'Received data : {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node  = ROBUSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()