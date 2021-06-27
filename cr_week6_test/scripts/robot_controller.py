#!/usr/bin/env python
import rospy
from cr_week6_test.msg import perceived_info
from cr_week6_test.msg import robot_info
from cr_week6_test.srv import predict_robot_expression
global PubExpression

def service(perception_info):
    rospy.wait_for_service('RobotExpressionPrediction')
    PubExpression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    print("Request")
    rospy.loginfo(perception_info)
    try:
        Predict = rospy.ServiceProxy('RobotExpressionPrediction', predict_robot_expression)
        z = Predict(perception_info)
        PubExpression.publish(z.prediction)  # publish object to topic IntTopicObject
        print("Prediction")
        rospy.loginfo(z.prediction)

    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def listener():
    PubExpression = rospy.Publisher("Robot_Expression", robot_info, queue_size=10)
    rospy.init_node('Robot_Controller', anonymous=True)
    rospy.Subscriber("Perceived", perceived_info, service)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
