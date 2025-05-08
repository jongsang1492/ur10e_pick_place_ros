#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg
from moveit_commander.planning_scene_interface import PlanningSceneInterface
import time

rospy.init_node("ur10e_add_box_node", anonymous=True)
moveit_commander.roscpp_initialize([])

scene = PlanningSceneInterface()
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

rospy.sleep(2)  # scene 초기화 기다림

# 박스 이름 정의
box_name = "obstacle_box"

# 박스 포즈 정의 (로봇 정면 0.35m 앞에 있는 장애물)
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = robot.get_planning_frame()
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.x = 0.4
box_pose.pose.position.y = -0.35
box_pose.pose.position.z = 0.15

# 박스 추가 (사이즈: 20cm x 20cm x 20cm)
scene.add_box(box_name, box_pose, size=(0.2, 0.2, 0.2))

rospy.loginfo("박스 추가 완료!")

