#!/usr/bin/env python3
import rospy
import moveit_commander
import geometry_msgs.msg
import time

rospy.init_node("ur10e_pick_place_path_node", anonymous=True)
moveit_commander.roscpp_initialize([])

robot = moveit_commander.RobotCommander()
group = moveit_commander.MoveGroupCommander("manipulator")

group.set_planning_time(5.0)
group.set_num_planning_attempts(10)

# 현재 상태에서 시작
group.set_start_state_to_current_state()

# Pose 정의 함수
def make_pose(x, y, z):
    pose = geometry_msgs.msg.Pose()
    pose.position.x = x
    pose.position.y = y
    pose.position.z = z
    pose.orientation.w = 1.0
    return pose

# Waypoints 만들기
waypoints = []

# 1️⃣ Pick 위치
pick_pose = make_pose(0.4, 0.0, 0.3)
waypoints.append(pick_pose)

# 2️⃣ 중간 경유지 (쭉 뻗은 팔 위치)
mid_pose = make_pose(0.35, 0.15, 0.25)
waypoints.append(mid_pose)

# 3️⃣ Place 위치
place_pose = make_pose(0.3, 0.3, 0.2)
waypoints.append(place_pose)

# 경로 계획
(plan, fraction) = group.compute_cartesian_path(
    waypoints,
    0.02,
    True
)

if fraction > 0.9:
    rospy.loginfo("경로 생성 성공! 실행 시작")
    group.execute(plan, wait=True)
    group.stop()
    group.clear_pose_targets()
else:
    rospy.logwarn("경로 생성 실패! fraction: %.2f", fraction)

