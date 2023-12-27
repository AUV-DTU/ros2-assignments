# Assignment 3
## Problem statement:
Create a `colcon` package `<your-name>_align_bot` which contains three nodes:

- `camera_publisher.py` - This node will start up the webcam and publish the frames to the topic `/camera/image_raw` and with every frame should output "Publishing video frame".
- `camera_subscriber.py` - This node will subscribe to `/camera/image_raw` , detect an object of an arbitary colour of your choice and then publish the coordinates of importance to the topic `/nav/heading`.
- `calculate_deviation.py`- This node will subscribe to `/nav/heading` and then calculate the deviation along the yaw axis and output it using `ROS_INFO`.  

### Instructions: Creating the package
- Follow the [ROS2 Humble documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to create the workspace.
- Navigate to the src directory and create a package `<your-name>_align_bot`.
- Create the nodes and build the package.

### Steps to Submit Assignment
* Fork the `ros2-assignments` repository
* Clone the forked repository to your machine `git clone "url you just copied"`
* Change to the repository directory on your computer
* Now create a branch using the git switch command `git switch -c <your-branch-name>`
* Add the package you've created into the assignment-3 folder
* `git add .`
* `git commit -m "<your-name> submitted"`
* Push your changes using the command git push `git push -u origin <your-branch-name>`
* Go to your repository on GitHub, you'll see a Compare & pull request button. Click on that button.
* Now submit the pull request.
* You can go ahead and delete your fork of this repository.