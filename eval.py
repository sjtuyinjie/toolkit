import re
from math import *
import os
import json

import matplotlib.pyplot as plt
import numpy as np
cnt=0
N=0
SR=0
SPL=0
SNA=0
for filea in os.listdir("./non_distractor/"):
    basedir="./non_distractor/"+filea


    for file in os.listdir(basedir):
        N+=1
        cnt+=1
        f1 = open("./non_distractor/"+filea+'/'+file, 'r')
        line=f1.readline()

        while line:
            if 'false' in line:
                break
            SR+=1
            user_dict = json.loads(line)
            print(filea+'/'+file)
            distance=float(user_dict["distance"])
            steps = float(user_dict["steps"])
            first_seen = float(user_dict["first_seen"])
            first_seen_dis=float(user_dict["first_seen_dis"])
            if(distance==0):
                SPL+=1
                SNA+=1
            else:
                SPL+=first_seen_dis/distance
                SNA+=first_seen/steps


            line=f1.readline()

print(cnt)
print(SR/cnt)
print(SPL/cnt)
print(SNA/cnt)
