# ROS-Turtlesim
# ROS Turtlesim - Circular Motion Task

This repository contains a ROS Python script to control the turtlesim robot, making it continuously move in a circular path.

## Code Overview
The script publishes geometry_msgs/Twist velocity messages to the /turtle1/cmd_vel topic with:
- Linear Velocity (x): 2.0
- Angular Velocity (z): 1.0

## How to Run

1. Start ROS Core:
   roscore

2. Launch Turtlesim Node:
   rosrun turtlesim turtlesim_node

3. Run the Script:
   python3 circle.py

## Results





https://github.com/user-attachments/assets/c81d5f3d-4711-4b0c-a732-dad90c8df357

