UR10e Pick and Place Project (ROS + MoveIt)

This project demonstrates a pick-and-place operation using the Universal Robots UR10e robotic arm in a simulated environment. The system was implemented using ROS Noetic and MoveIt, and programmed in Python.

[![Watch the demo](./imgs/screenshot.png)](./videos/ros_ur10e_pick_place_demo.mp4)

FEATURES:
- Cartesian path planning with multiple waypoints
- Motion execution with collision checking
- Obstacle (box) insertion into the planning scene
- ROS-integrated control using MoveIt Commander (Python API)

HOW TO RUN:
cd ~/catkin_ws
catkin_make
source devel/setup.bash
roslaunch ur10e_moveit_config demo.launch
rosrun ur10e_control ur10e_pick_place.py
*For obstacle: run ur10e_add_box.py before pick_place.py*

PROJECT STRUCTURE:
ur10e_pick_place_ros/
├── scripts/
│   ├── ur10e_add_box.py
│   ├── ur10e_move.py
│   ├── ur10e_pose.py
│   └── ur10e_pick_place.py
├── videos/
│   └── ros_ur10e_pick_place_demo.mp4
├── imgs/
│   └── screenshot.png
└── README.md

TECH STACK:
-ROS Noetic
-MoveIt
-Python 3
-RViz
-UR10e MoveIt package

Author
Jongsang Yoo
Mechanical Engineering @ University of Toronto
GitHub: @jongsang1492
