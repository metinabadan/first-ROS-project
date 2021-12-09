#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
from os import name
import rospy
import actionlib
import ilk_paket.msg
import sys

def fibonacci_client():
    client = actionlib.SimpleActionClient('fibonacci',ilk_paket.msg.FibonacciAction)
    client.wait_for_server()

    goal = ilk_paket.msg.FibonacciGoal(order = 20)

    client.send_goal(goal)
    client.wait_for_result()

    return client.get_result()

if __name__ == "__main__":
    try:
        rospy.init_node('action_client')
        result = fibonacci_client()
        print('sonuc:', ', '.join([str(n) for n in result.sequence]))
    except rospy.ROSInterruptException:
        print("islem tamamlanamadi",file=sys.strderr)