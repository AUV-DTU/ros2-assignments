# Assignment 1
## Problem statement:
Create a `colcon` package `<your-name>_prime_composite` which contains two nodes:

- `random_number_publisher.cpp/random_number_publisher.py` - This node will publish random integers to a ROS topic named `topic_numbers`.
- `prime_composite_classifier.cpp/prime_composite_classifier.py` - This node will subscribe to `topic_numbers` and classify the published integer as either prime or composite and output the classification using ROS_INFO.

### Instructions: Creating the package
- Follow the [ROS2 Humble documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to create the workspace.
- Navigate to the src directory and create a package `<your-name>_prime_composite`.
- Create the nodes and build the package.

### Steps to Submit Assignment
* Fork the `ros2-assignments` repository
* Clone the forked repository to your machine `git clone "url you just copied"`
* Change to the repository directory on your computer
* Now create a branch using the git switch command `git switch -c <your-branch-name>`
* Add the package you've created into the assignment-1 folder
* `git add .`
* `git commit -m "<your-name> submitted"`
* Push your changes using the command git push `git push -u origin <your-branch-name>`
* Go to your repository on GitHub, you'll see a Compare & pull request button. Click on that button.
* Now submit the pull request.