#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/int32.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"

using std::placeholders::_1;

#include <opencv2\opencv.hpp>

class framedetector: public rclcpp::Node
{
  public:
    framedetector()
    : Node("framedetector")
    {
      subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
      "frame", 10, std::bind(&framedetector::topic_callback, this, _1));
    }

  private:
    void detectblue(Mat dil,Mat img)
    {
        vector<vector<Point>> contours;
        vector<Vec4i> hierarchy;

        findContours(dil, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
        drawContours(img, contours, -1, Scalar(0,0,255), 2);

    }
    void topic_callback(const sensor_msgs::msg::Image & msg) const
    { 
        Mat mask,hsv_img,blur,imgcan,dil;
        
        auto frame = msg;
        cv::cvtColor(frame, hsv_img,COLOR_BGR2HSV);

        Scalar lower(110,50,50);
        Scalar upper(130,255,255);
        inRange(hsv_img, lower, upper, mask);
        Gaussianblur(mask,blur,Size(3,3),3,0);
        Canny(blur, imgcan,25,75);
        Mat kernel = getStructuringElement(MORPH_RECT,Size(3,3));
        dilate(imgcan,dil,kernel);

        detectblue(dil, frame);

        while(true)
        {
            imshow("Webcam", frame);
            waitKey(0);
        }
        
        RCLCPP_INFO(this->get_logger(), "Detecting Blue in Every frame");
        

    }
    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<framedetector>());
  rclcpp::shutdown();
  return 0;
}