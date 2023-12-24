# Assignment 2
## Problem statement:
Create a `colcon` package `<your-name>_opencv_setup` which contains two nodes:

- `webcam_publisher.py` - This node will start up the webcam and publish the frames to the topic `/camera/image_raw` and with every frame should output "Publishing video frame".
- `webcam_subscriber.py` - This node will subscribe to `/camera/image_raw` and should form contours over any object of blue colour present in the video feed.With every frame , you should output "Receiving Video Feed".

### Instructions: Creating the package
- Follow the [ROS2 Humble documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to create the workspace.
- Navigate to the src directory and create a package `<your-name>_opencv_setup`.
- Create the nodes and build the package.

### Steps to Submit Assignment
* Fork the `ros2-assignments` repository
* Clone the forked repository to your machine `git clone "url you just copied"`
* Change to the repository directory on your computer
* Now create a branch using the git switch command `git switch -c <your-branch-name>`
* Add the package you've created into the assignment-2 folder
* `git add .`
* `git commit -m "<your-name> submitted"`
* Push your changes using the command git push `git push -u origin <your-branch-name>`
* Go to your repository on GitHub, you'll see a Compare & pull request button. Click on that button.
* Now submit the pull request.