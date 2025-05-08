#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg
from moveit_commander.planning_scene_interface import PlanningSceneInterface
import time

# Initialize the ROS node and MoveIt commander
rospy.init_node("ur10e_add_box_node", anonymous=True)
moveit_commander.roscpp_initialize([])

scene = PlanningSceneInterface()
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

rospy.sleep(2)  # Wait for the planning scene to initialize

# Define the box name
box_name = "obstacle_box"

# Define the pose of the box (an obstacle placed 0.35m in front of the robot)
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = robot.get_planning_frame()
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.x = 0.4
box_pose.pose.position.y = -0.35
box_pose.pose.position.z = 0.15

# Add the box to the planning scene (size: 20cm x 20cm x 20cm)
scene.add_box(box_name, box_pose, size=(0.2, 0.2, 0.2))

rospy.loginfo("Box added to the planning scene!")
