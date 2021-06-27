#!/usr/bin/env python
import rospy
import numpy as np
from cr_week6_test.msg import object_info
from cr_week6_test.msg import human_info
from cr_week6_test.msg import perceived_info
global Publish_Filter

def callback_Object(data):
    pass

def callback_Human(data):
    pass

def callback_perception(data):
    ## Random integer generation
    random_filter = np.random.randint(1,8)
    rospy.loginfo(random_filter)
   
    if random_filter == 1:
        data.object_size = 0

    elif random_filter == 2:
        data.human_action = 0

    elif random_filter == 3:
        data.human_expression = 0

    elif random_filter == 4:
        data.object_size = 0
        data.human_action = 0

    elif random_filter == 5:
        data.object_size = 0
        data.human_expression = 0

    elif random_filter == 6:
        data.human_action = 0
        data.human_expression = 0

    elif random_filter == 7:
        data.object_size = 0
        data.human_action = 0
        data.human_expression = 0
        
    rospy.loginfo(data)
    Publish_Filter.publish(data)


def listener():
    rospy.init_node('Perception_Filter', anonymous=True)
    rospy.Subscriber("IntTopicObject", object_info, callback_Object)
    rospy.Subscriber("IntTopicHuman", human_info, callback_Human)
    rospy.Subscriber("IntTopicGenerate", perceived_info, callback_perception)
    rospy.spin()

if __name__ == '__main__':
    Publish_Filter = rospy.Publisher("Perceived", perceived_info, queue_size=10)
    listener()
