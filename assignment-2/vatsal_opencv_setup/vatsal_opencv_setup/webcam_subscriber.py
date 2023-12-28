# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
import cv2

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge 

class MinimalSubscriber(Node):

    def detect_and_draw_contours(self, frame):
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])


        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        result_frame = frame.copy()
        cv2.drawContours(result_frame, contours, -1, (0, 255, 0), 2)

        # Display the original and result frames
        cv2.imshow('Original', frame)
        cv2.imshow('Blue Contours', result_frame)

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'image_raw', 
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        
        bridge = CvBridge()
        frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        
        self.detect_and_draw_contours(frame)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
