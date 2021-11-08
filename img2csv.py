
#for euroc    structvio
import os, sys,re,csv
name="room_dark_02"
# basedir="/media/yinjie/2498AF1F98AEEF0C/adataset/15results/imu_bagtxt/"+name+'.txt'
# txtdir="/media/yinjie/2498AF1F98AEEF0C//adataset/15results/imu_orbtxt/"+name+'.txt'
#basedir="/media/yinjie/2498AF1F98AEEF0C/adataset/15results/imu_bagtxt/"+name+'.txt'
#basedir="/media/car/2498AF1F98AEEF0C/big/cam_imu/"+name+'.txt'
basedir='/media/yinjie/harddisk/struct/'+name
dstdir='/media/yinjie/2498AF1F98AEEF0C/adataset/gtmid/euroc_img_csv/'+name+'.csv'
#timedir="/media/yinjie/2498AF1F98AEEF0C/big/cam_imu/"+name+'_time.txt'
# with open('test.csv','w')as fcsv:
#     f_csv = csv.writer(f_csv)
#     f_csv.writerow(headers)

fcsv=open(dstdir,'w')
f_csv = csv.writer(fcsv)


line2or=['#timestamps[ns]','filename']
f_csv.writerow(line2or)
for filename in sorted(os.listdir(basedir+'/cam0/data/')):
    
    time=filename[0:19]
    #print(time)
    #break
    line2or=[time,filename]
    f_csv.writerow(line2or)
    #time=filename[0:10]+'.'+filename[10:19]
    #f.write(time+' imgs/cam0/img'+str(cnt)+'.png imgs/cam1/img'+str(cnt)+'.png imgs/cam2/img'+str(cnt)+'.png\n')
    #f.write(time+' imgs/cam0/img'+str(cnt)+'.png\n')
    #cnt+=1
# while line:
#     line=line.split(',')
#     linetor=[line[0],line[1],line[2],line[3],line[4],line[5],line[6].replace('\n', '').replace('\r', '')]
#     # print(linetor)
#     # break
#     f_csv.writerow(linetor)
#     line=f1.readline()