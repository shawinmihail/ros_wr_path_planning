#!/usr/bin/env python
import rospy
from wr_msgs.msg import route_line
from geometry_msgs.msg import Vector3
from time import sleep
import numpy as np

def spawner():
    pub = rospy.Publisher('kin_model/route_input', route_line, queue_size=1)
    rospy.init_node('kin_model_spawner_node')
    rate = rospy.Rate(1) # 10hz
    sleep(5)
    
    msg = route_line()
    eps = 0.01;
    for i in range(20):
        v = Vector3()
        v.x = 20 * np.sin(2 * 3.1415 * i / 20.0)
        v.y = 30 * np.cos(2 * 3.1415 * i / 20.0)
        v.z = surf(v.x, v.y) + eps
        msg.points.append(v)
        

    pub.publish(msg)
    
    #while not rospy.is_shutdown():
        #pub.publish(msg)
        #rate.sleep()
        #break
        
def surf(x, y):
    z = 4.7015322203620275587354626622982*np.sin(0.038554389187938227010841212547509*x - 0.29309335149430976175111140946683) + 2.2321880997147411918035686539952*np.sin(0.036294060916760320743550600916685*y - 0.33043646669624404665910333278589) + 2.0214791347991996062205544149037*np.sin(0.035547774491341650861689538128696*x + 1.4307820067067456015763582399813) - 1.2745563470986207565971426447504*np.sin(0.036828840049009814485283280953887*y + 0.48399372981007465766012387575756)
    return z
        

if __name__ == '__main__':
    try:
        spawner()
    except rospy.ROSInterruptException:
        pass
