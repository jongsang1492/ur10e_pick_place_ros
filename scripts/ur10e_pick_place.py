#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg
import time

# Initialize the ROS node and MoveIt commander
rospy.init_node("ur10e_pick_place_path_node", anonymous=True)
moveit_commander.roscpp_initialize([])

robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

group.set_planning_time(5.0)
group.set_num_planning_attempts(10)

# Set the initial state to the current robot state
group.set_start_state_to_current_state()

# Helper function to create a pose with specified coordinates
def make_pose(x, y, z):
    pose = geometry_msgs.msg.Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z
    pose.orientation.w = 1.0
    return pose

# Create a list of waypoints
waypoints = []

# 1️⃣ Pick position
pick_pose = make_pose(0.4, 0.0, 0.3)
waypoints.append(pick_pose)

# 2️⃣ Intermediate waypoint (arm extended forward)
mid_pose = make_pose(0.35, 0.15, 0.25)
waypoints.append(mid_pose)

# 3️⃣ Place position
place_pose = make_pose(0.3, 0.3, 0.2)
waypoints.append(place_pose)

# Plan a Cartesian path through the waypoints
(plan, fraction) = group.compute_cartesian_path(
    waypoints,
    0.02,  # eef_step (path resolution)
    True   # avoid_collisions
)

if fraction > 0.9:
    rospy.loginfo("Path planning successful! Executing the trajectory.")
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
else:
    rospy.logwarn("Path planning failed. fraction: %.2f", fraction)
