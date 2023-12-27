#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <cstdlib>
#include <ctime>

#include "std_msgs/msg/int32.hpp"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"

//#include "std_msgs/msg/string.hpp"

#include "opencv2\opencv.hpp"


using namespace std::chrono_literals;

class webcam : public rclcpp::Node
{
    public:
        webcam(): Node("Frame")
        {
            publisher_ = this->create_publisher<sensor_msgs::msg::Image>("frame", 10);
            timer_ = this->create_wall_timer(
            100ms, std::bind(&webcam::timer_callback, this));
            cap_ = cv::VideoCapture(0);
        }
    private:
        void timer_callback()
        {
            cv::Mat img;
            cap >> img;
            auto img_msg = cv_bridge::CvImage(std_msgs::msg::Header(), "bgr8", frame).toImageMsg();
            RCLCPP_INFO(this->get_logger(), "Publishing Frame");
            publisher_->publish(*img_msg);
        
        }
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Publisher<sensor_msgs::msg::image >::SharedPtr publisher_;
        cv::VideoCapture cap_;

};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<webcam>());
    rclcpp::shutdown();
    return 0;
}




