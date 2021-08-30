#!/usr/bin/env python

import cv2
import time
import rospy
#from std_msgs.msg import
#from beginner_tutorials.msg import Image
from sensor_msgs.msg import Image
#from Image.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import  cv_bridge
import numpy as np

#from PIL import Image 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
#cap.set(cv2.VideoWriter_fourcc(*'XVID'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
#cap.set(cv2.CAP_PROP_FOURCC, cv2.cv.FOURCC('M','J','P','G'))
#out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))
def thermal_publisher():
    pub = rospy.Publisher('thermal_image_raw',Image , queue_size=10)
    rospy.init_node('thermal_publisher', anonymous=True)
    rate = rospy.Rate(25) # 10hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        #cv2.imshow("thermal", frame)
        #print(frame)
        #im = np.frombuffer(frame.data, dtype=np.uint8).reshape(512, 640, -1)
        #im=Image.fromarray(frame)
        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(frame, encoding="passthrough")
        #http://docs.ros.org/en/api/sensor_msgs/html/msg/Image.html
        #pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))
        #image_message.
        image_message.header.stamp.secs=int(time.time())#int向下取整
        #print(int(time.time()))
        #print(int((time.time()-int(time.time()))*1000000000))
        image_message.header.stamp.nsecs=int((time.time()-int(time.time()))*1000000000)
        pub.publish(image_message)
        #print(time.time())
        rate.sleep()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)


if __name__ == '__main__':
    try:
        thermal_publisher()
    except rospy.ROSInterruptException:
        pass


 
cap.release()
cv2.destroyAllWindows()
