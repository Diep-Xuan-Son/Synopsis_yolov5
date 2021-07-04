import cv2
import numpy as np
import glob, os
from natsort import natsorted
import sqlite3
from utils.plots import plot_one_box

def plot(x1, y1, x2, y2, time, obj, frame, classes, filename):
    img0 = cv2.imread('./datasynopsis2/ROI_' + str(frame) +'.jpg')
    xyxy = [x1, y1, x2, y2]
    label = f'{classes} {time}'
    plot_one_box(xyxy, img0, label=label, color=(208, 224, 64) , line_thickness=1)
    return img0
# def CreateVideo(fps):
# 	print("Creating Video...")
# 	img_array = []
# 	n= 0
# 	dataset_path = "/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynopsis2"
# 	# # print(glob.glob('/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynoSpsis/*.jpg', recursive=True))
# 	for filename in natsorted(glob.iglob(os.path.join(dataset_path, "*.jpg"))):
# 	    img = cv2.imread(filename)
# 	    # cv2.imshow('adf',img)
# 	    # cv2.waitKey()
# 	    height, width, layers = img.shape
# 	    size = (width,height)
# 	    img_array.append(img)
# 	out = cv2.VideoWriter('./video/project4.avi',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
# 	# *'DIVX'
# 	for i in range(len(img_array)):
# 	    out.write(img_array[i])
# 	cv2.destroyAllWindows()
# 	out.release()		
# 	print("Done!")
confil = sqlite3.connect('filter.db')
curfil = confil.cursor()

v = cv2.VideoCapture('video4.mp4')
numFrame = v.get(cv2.CAP_PROP_FRAME_COUNT)
fps = v.get(cv2.CAP_PROP_FPS) 

# def CreateVideo(fps):
print("Creating Video...")
img_array = []
n= 0
dataset_path = "/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynopsis2"
# # print(glob.glob('/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynoSpsis/*.jpg', recursive=True))
img0 = cv2.imread("./datasynopsis1/IBG.jpg")
height0, width0, layers0 = img0.shape
size0 = (width0,height0)
out = cv2.VideoWriter('./video/project10.avi',cv2.VideoWriter_fourcc(*'mp4v'), fps, size0)
for filename in natsorted(glob.iglob(os.path.join(dataset_path, "*.jpg"))):
    for rowfil in curfil.execute('SELECT * FROM filter '):
        if(str(rowfil[6]) == filename[58:-4]):
            img = plot(rowfil[0], rowfil[1], rowfil[2], rowfil[3], rowfil[4], rowfil[5], rowfil[6], rowfil[7], filename)
            out.write(img)
            break
# for i in range(len(img_array)):
#     out.write(img_array[i])
cv2.destroyAllWindows()
out.release()		
print("Done!")
