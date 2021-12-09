#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import actionlib
import ilk_paket.msg

class FibonacciAction(object):
    feed_back = ilk_paket.msg.FibonacciFeedback()
    sonuc = ilk_paket.msg.FibonacciResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("fibonacci",ilk_paket.msg.FibonacciAction,execute_cb=self.execute_cb,auto_start=False)
        self._as.start()

    def execute_cb(self,goal):
        r = rospy.Rate(1)
        self.feed_back.sequence = []
        self.feed_back.sequence.append(0)
        self.feed_back.sequence.append(1)

        rospy.loginfo('Calisiyor... Fibonacci dizisi olusturuluyor, hedef = %i , baslangic: %i , %i',goal.order,self.feed_back.sequence[0],self.feed_back.sequence[1])

        for i in range(1,goal.order):
            self.feed_back.sequence.append(self.feed_back.sequence[i] + self.feed_back.sequence[i-1])
            self._as.publish_feedback(self.feed_back)
        
        self.sonuc.sequence = self.feed_back.sequence
        rospy.loginfo('BASARİLİ')
        self._as.set_succeeded(self.sonuc)

if __name__ == "__main__":
    rospy.init_node('action_server')

    server = FibonacciAction()

    rospy.spin()