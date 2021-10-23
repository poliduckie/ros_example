#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import WheelsCmdStamped

def talker():
    pub = rospy.Publisher("/duckvader/wheels_driver_node/wheels_cmd", Person)
    rospy.init_node('go_straight_test', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = WheelsCmdStamped()
    msg.vel_left = 0.5
    msg.vel_right = 0.5

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
