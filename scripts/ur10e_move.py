#!/usr/bin/env python3
import rospy
import moveit_commander

rospy.init_node("ur10e_motion_node", anonymous=True)
moveit_commander.roscpp_initialize([])

robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

joint_goal = group.get_current_joint_values()
joint_goal[1] -= 0.5

group.set_joint_value_target(joint_goal)
group.go(wait=True)

group.stop()
group.clear_pose_targets()
