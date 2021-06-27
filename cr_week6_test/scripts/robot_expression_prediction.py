#!/usr/bin/env python
import rospy
from cr_week6_test.msg import perceived_info
from cr_week6_test.msg import robot_info
from cr_week6_test.srv import predict_robot_expression
import random
from bayesian_belief_networks.ros_utils import *

def human_expression_prob(human_expression):
    return 0.33
def human_action_prob(human_action):
    return 0.33
def object_size_prob(object_size):
    return 0.50


## Implementation of conditional probability table
def Happy(human_expression, human_action, object_size):
    table = dict()
    table['HRS'] = 0.8
    table['HRB'] = 1.0
    table['HOS'] = 0.8
    table['HOB'] = 1.0
    table['HAS'] = 0.6
    table['HAB'] = 0.8
    table['SRS'] = 0
    table['SRB'] = 0
    table['SOS'] = 0
    table['SOB'] = 0.1
    table['SAS'] = 0
    table['SAB'] = 0.2
    table['NRS'] = 0.7
    table['NRB'] = 0.8
    table['NOS'] = 0.8
    table['NOB'] = 0.9
    table['NAS'] = 0.6
    table['NAB'] = 0.7

    key = ''
    if human_expression == 1:
        key = key + 'Happy'
    elif human_expression == 2:
        key = key + 'Sad'
    else:
        key = key + 'Neutral'

    if human_action == 1:
        key = key + 'Looking at Robot'
    elif human_action == 2:
        key = key + 'Object'
    else:
        key = key + 'Away'

    if object_size == 1:
        key = key + 'Small'
    else:
        key = key + 'Big'
    return table[key]


def Sad(human_expression, human_action, object_size):
    table = dict()
    table['HRS'] = 0.2
    table['HRB'] = 0
    table['HOS'] = 0.2
    table['HOB'] = 0
    table['HAS'] = 0.2
    table['HAB'] = 0.2
    table['SRS'] = 0
    table['SRB'] = 0
    table['SOS'] = 0.1
    table['SOB'] = 0.1
    table['SAS'] = 0.2
    table['SAB'] = 0.2
    table['NRS'] = 0.3
    table['NRB'] = 0.2
    table['NOS'] = 0.2
    table['NOB'] = 0.1
    table['NAS'] = 0.2
    table['NAB'] = 0.2

    key = ''
    if human_expression == 1:
        key = key + 'Happy'
    elif human_expression == 2:
        key = key + 'Sad'
    else:
        key = key + 'Neutral'

    if human_action == 1:
        key = key + 'Looking at Robot'
    elif human_action == 2:
        key = key + 'Object'
    else :
        key = key + 'Away'

    if object_size == 1:
        key = key + 'Small'
    else:
        key = key + 'Big'
    return table[key]


def Neutral(human_expression, human_action, object_size):
    table = dict()
    table['HRS'] = 0
    table['HRB'] = 0
    table['HOS'] = 0
    table['HOB'] = 0
    table['HAS'] = 0.2
    table['HAB'] = 0
    table['SRS'] = 1
    table['SRB'] = 1
    table['SOS'] = 0.9
    table['SOB'] = 0.8
    table['SAS'] = 0.8
    table['SAB'] = 0.6
    table['NRS'] = 0
    table['NRB'] = 0
    table['NOS'] = 0
    table['NOB'] = 0
    table['NAS'] = 0.2
    table['NAB'] = 0.1

    key = ''
    if human_expression == 1:
        key = key + 'Happy'
    elif human_expression == 2:
        key = key + 'Sad'
    else:
        key = key + 'Neutral'

    if human_action == 1:
        key = key + 'Looking at Robot'
    elif human_action == 2:
        key = key + 'Object'
    else:
        key = key + 'Away'

    if object_size == 1:
        key = key + 'Small'
    else:
        key = key + 'Big'
    return table[key]

## Building the Bayesian Belief Network(BBN)
def Predictor(BBN):
    BBN = ros_build_bbn(
                 human_expression_prob,
                 human_action_prob,
                 Happy, Sad, Neutral)
    return BBN

def expression_prediction_server():
    rospy.init_node('robot_expression_prediction')  #node initialised
    serv = rospy.Service('RobotExpressionPrediction', predict_robot_expression, Predictor) #service started
    rospy.spin()

if __name__ == "__main__":
    expression_prediction_server()
