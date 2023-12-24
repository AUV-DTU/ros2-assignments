# Assignment 1
## Problem statement:
Create a `colcon` package `<github-username>_prime_composite` which contains two nodes:

- `random_number_publisher.cpp/random_number_publisher.py` - This node will publish random integers to a ROS topic named `topic_numbers`.
- `prime_composite_classifier.cpp/prime_composite_classifier.py` - This node will subscribe to `topic_numbers` and classify the published integer as either prime or composite and output the classification using ROS_INFO.