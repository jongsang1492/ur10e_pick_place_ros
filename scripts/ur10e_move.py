#!/usr/bin/env python3
import rospy
import moveit_commander

# Initialize the ROS node and MoveIt commander
rospy.init_node("ur10e_motion_node", anonymous=True)
moveit_commander.roscpp_initialize([])

robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

# Get current joint values
joint_goal = group.get_current_joint_values()

# Move the second joint downward by 0.5 radians
joint_goal[1] -= 0.5

# Set the target joint values and execute the motion
group.set_joint_value_target(joint_goal)
group.go(wait=True)

# Stop any residual movement and clear targets
group.stop()
group.clear_pose_targets()
