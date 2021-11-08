# coding:utf-8
# !/usr/bin/python

# Extract images from a bag file.

# PKG = 'beginner_tutorials'
import roslib  # roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import numpy as np
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
from matplotlib import pyplot as plt
# Reading bag filename from command line or roslaunch parameter.
# import os
import sys

path='your_path'#bag包路径, /结尾
filename='lift_04'
# cameras=['camera1','camera2']

topic_names={'rgb_topics':['/camera/color/image_raw/compressed']
             }
cam_rgb_path=[path+'/euroc/'+filename+'/mav0/cam0/data/']


# for camPath in cam_rgb_path:
#     print(camPath)
if os.path.exists(path+filename+'.bag'):
    for path_dir in cam_rgb_path:
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)

else:
    print('bag file not exist!!')
    sys.exit()

class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        print("Waiting......")

        with rosbag.Bag(path+filename+'.bag','r') as bag:  # 要读取的bag文件；
            for topic, msg, t in bag.read_messages():
                for i in range(len(topic_names['rgb_topics'])):
                    if topic == topic_names['rgb_topics'][i]:  # 图像的topic；
                        try:
                            cv_image=self.bridge.compressed_imgmsg_to_cv2(msg)
                            #cv_image = self.bridge.imgmsg_to_cv2(msg,'bgr8')
                            # a = np.fromstring(msg.data, dtype=np.uint8)
                            # print("/sensor/hugo1/image1/compressed \n")
                            # print(a.size)
                            # # print(a.shape)
                            # print(a[0:6])
                            # img = a.reshape(1280,720,3)
                            # cv_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                            # cv_image = cv2.imdecode(a, 1)
                            # cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print (e)
                        timestr = "%.9f" % msg.header.stamp.to_sec()
                        # %.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr.replace('.','') + ".png"  # 图像命名：时间戳.png
                        
                        cv2.imwrite(cam_rgb_path[i]+image_name , cv_image)  # 保存；

                

if __name__ == '__main__':
    # rospy.init_node(PKG)
    try:
        image_creator = ImageCreator()
        print("done")
    except rospy.ROSInterruptException:
        pass
