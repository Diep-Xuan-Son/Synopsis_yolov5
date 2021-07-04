import sqlite3
from PIL import Image, ImageDraw, ImageFilter
from utils.plots import plot_one_box
import cv2
import numpy as np
import glob, os
from natsort import natsorted
import createVideo_30
import data_labels_30
import subprocess
import cv2

subprocess.call(["python3", "detect_data_30.py", "--weights", "person4.pt", "--img", "640", "--conf", "0.25", "--source", "video6.mp4", "--device", "0"])
v = cv2.VideoCapture('video6.mp4')
numFrame = v.get(cv2.CAP_PROP_FRAME_COUNT)
fps = v.get(cv2.CAP_PROP_FPS) 
t0 = numFrame/fps/60
data_labels_30.data_labels_30(t0)
createVideo_30.CreateVideo_30(round(fps))