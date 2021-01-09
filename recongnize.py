import cv2 as cv
import numpy as np
#读取文件内容
cap = cv.VideoCapture("test.mp4")
#获取文件视频帧数和帧内容
ret, frame = cap.read()
#获取图片的通道和大小数值
count=frame.shape
#显示对应的图像数值情况
print(count[0],count[1])
#改变图像大小
length =int(count[0]/4)
high =int(count[1]/4)
print(length,high)
#计算对应的比例
f_zong = 0
f_lv = 0
zong = 0
zong1 = 0
#开始读取图片
while(ret):
#图像需要进行缩减，保存关键信息就行，处理不需要全部考虑上
#对应进行对应的转换关系对应的是宽度和长度转换
    frame = cv.resize(frame, (high,length), interpolation=cv.INTER_CUBIC)
#分割图像BGR图像-对应蓝色-绿色-红色
    b, g, r = cv.split(frame)
#计算像素的值均值并且输出
    #初始化整个像素和的值
    #print(g.shape)
    zong1 = zong
    zong = 0
    for x in range(0,length):
        for y in range(0,high):
            zong = zong + g[x,y]
    #print(zong)
#显示图片内容
#计算闪烁频率和计算总时间是不一样的，只是一半一半的占用情况
    f_zong = f_zong +1
    if abs(zong1-zong) >5000000:
        f_lv = f_lv +1
    #cv.imshow("capture", g)
#是否延迟和对应的是否退出
    #if cv.waitKey(1) & 0xFF == ord('q'):
        #break
#读取图片和对应的读取图像内容
    ret, frame = cap.read()
#关闭图像采集设备
cap.release()
#关闭窗口
cv.destroyAllWindows() 
#输出最终的结果
print(f_zong)
print(f_lv)