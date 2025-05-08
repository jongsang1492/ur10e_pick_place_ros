#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg

# Initialize the ROS node
rospy.init_node("ur10e_pose_move_node", anonymous=True)
moveit_commander.roscpp_initialize([])

# Create MoveIt Commander interfaces
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

# Clear any previous targets and stop residual movement
group.stop()
group.clear_pose_targets()

# Define the target pose (example pick position)
target_pose = geometry_msgs.msg.Pose()
target_pose.position.x = 0.4
target_pose.position.y = 0.0
target_pose.position.z = 0.3
target_pose.orientation.w = 1.0  # Facing forward (simple orientation)

# Set the target pose and execute the motion
group.set_pose_target(target_pose)
success = group.go(wait=True)

# Final cleanup
group.stop()
group.clear_pose_targets()

# Print the result
if success:
    rospy.loginfo("Pose movement succeeded!")
else:
    rospy.logwarn("Pose movement failed!")
