import sqlite3
from PIL import Image, ImageDraw, ImageFilter
from utils.plots import plot_one_box
import cv2
import numpy as np
import glob, os
from natsort import natsorted
import createVideo
import data_labels
import subprocess

subprocess.call(["python3", "detect_data.py", "--weights", "person4.pt", "--img", "640", "--conf", "0.25", "--source", "video4.mp4", "--device", "0"])
v = cv2.VideoCapture('video4.mp4')
numFrame = v.get(cv2.CAP_PROP_FRAME_COUNT)
fps = v.get(cv2.CAP_PROP_FPS) 
t0 = numFrame/fps/60
data_labels.data_labels(t0)
createVideo.CreateVideo(round(fps))
