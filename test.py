#!/usr/bin/env python

import rospy
import actionlib
import tf
from math import pi

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def goal_pose(pose):  # Convert from waypoints into goal positions
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose


if __name__ == '__main__':
    rospy.init_node('move_test')

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  # Creates the Action Client
    client.wait_for_server()
    
    while True:
        x, y, r = input("Input X, Y, θ : ").split()
        goal = goal_pose((x, y, 0.0), tf.transformations.quaternion_from_euler(0, 0, r*pi/180))
        client.send_goal(goal)
        print("Moving towards goal...")
        # client.wait_for_result(rospy.Duration.from_sec(2.0))
