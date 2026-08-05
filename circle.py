#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_circle():
    rospy.init_node('turtle_circle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 1.0

    while not rospy.is_shutdown():
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass
