#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg

# 노드 초기화
rospy.init_node("ur10e_pose_move_node", anonymous=True)
moveit_commander.roscpp_initialize([])

# MoveIt Commander 객체 생성
robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

# 현재 상태 초기화
group.stop()
group.clear_pose_targets()

# 이동할 위치 정의 (Pick 위치 예시)
target_pose = geometry_msgs.msg.Pose()
target_pose.position.x = 0.4
target_pose.position.y = 0.0
target_pose.position.z = 0.3
target_pose.orientation.w = 1.0  # 간단하게 정면 방향

# 목표 pose 설정하고 이동
group.set_pose_target(target_pose)
success = group.go(wait=True)

# 마무리
group.stop()
group.clear_pose_targets()

# 결과 출력
if success:
    rospy.loginfo("Pose 이동 성공!")
else:
    rospy.logwarn("Pose 이동 실패!")

