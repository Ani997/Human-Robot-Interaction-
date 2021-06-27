#!/usr/bin/env python
import rospy
import numpy as np
from cr_week6_test.msg import object_info
from cr_week6_test.msg import human_info
from cr_week6_test.msg import perceived_info


def interaction_generator():

    ## initializing the publisher topics
    Object_publish = rospy.Publisher("IntTopicObject", object_info, queue_size=10)
    Human_publish = rospy.Publisher("IntTopicHuman", human_info, queue_size=10)
    Overall_publish = rospy.Publisher("IntTopicGenerate", perceived_info, queue_size=10)  

    ## initialisation for generation of random messages
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.1)  

    ## initializing the message containers
    object_msg = object_info()
    human_msg = human_info()
    overall_msg = perceived_info()

    id_val = 0
    while not rospy.is_shutdown():

        id_val+=1

        ## object values assignment and publishing
        object_msg.object_size = np.random.randint(1,2)
        object_msg.id = id_val
        Object_publish.publish(object_msg)
        rospy.loginfo(object_msg)

        ## Human values assignment and publishing
        human_msg.id = id_val
        human_msg.human_expression = np.random.randint(1,3)
        human_msg.human_action = np.random.randint(1,3)
        Human_publish.publish(human_msg)
        rospy.loginfo(human_msg)

        ## Overall values assignment and publishing
        overall_msg.id = id_val
        overall_msg.object_size = object_msg.object_size
        overall_msg.human_action = human_msg.human_action
        overall_msg.human_expression = human_msg.human_expression
        rospy.loginfo(overall_msg)
        Overall_publish.publish(overall_msg)

        rate.sleep()


if __name__ == '__main__':
    try:
        interaction_generator()
    except rospy.ROSInterruptException:
        pass
