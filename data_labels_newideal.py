import sqlite3
from PIL import Image, ImageDraw, ImageFilter
from utils.plots import plot_one_box
import cv2

def plot(x1, y1, x2, y2, time, obj, frame, classes):
	img0 = cv2.imread('./datasynopsis2/ROI_' + str(frame) +'.jpg')
	xyxy = [x1, y1, x2, y2]
	label = f'{classes} {time}'
	plot_one_box(xyxy, img0, label=label, color=(255, 0, 0) , line_thickness=1)
	cv2.imwrite('./datasynopsis2/ROI_' + str(frame) +'.jpg', img0)

def aInRangebc(a,b,c):
	if(a>=b and a<=c):
		return True
	else:
		return False
# def data_labels(t0):
print("Running...")
n = 2
t = 5
data = []
c = 'person'
t1 = 0
i = 0
j = 0
k = 0
con = sqlite3.connect('dtsynopsis.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM stocks '):
	if((((float(row[4][0:1])*60 + float(row[4][2:7])) < (t*60/n)) or ((float(row[4][0:1])*60 + float(row[4][2:7])) < (t1 + 4))) and (row[7] == c) ):
		if(row[5] != 0):
			im1 = Image.open('./datasynopsis2/ROI_' + str(row[6]) + '.jpg')
			im3 = Image.open('./datasynopsis/ROI_' + str(row[6]) + '_' + str(row[5]) + '.jpg')
			im1.paste(im3, (int(row[0]), int(row[1])))
			im1.save('./datasynopsis2/ROI_' + str(row[6]) + '.jpg', quality=95)
			plot(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
		else:
			im1 = Image.open('./datasynopsis1/IBG.jpg')
			im2 = Image.open('./datasynopsis/ROI_' + str(row[6]) + '_0.jpg')
			im1.paste(im2, (int(row[0]), int(row[1])))
			im1.save('./datasynopsis2/ROI_' + str(row[6]) + '.jpg', quality=95)
			plot(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
		t1 = float(row[4][0:1])*60 + float(row[4][2:7])
		j = j + 1
		data.append([row[6], row[1], row[0], row[3], row[2]]) #ROI,y1,x1,y2,x2
	elif(((float(row[4][0:1])*60 + float(row[4][2:7])) >= (t*60/n)) and ((float(row[4][0:1])*60 + float(row[4][2:7])) >= (t1 + 4)) and row[7] == c):
		im1 = Image.open('./datasynopsis2/ROI_' + str(data[i][0]) + '.jpg')
		im2 = Image.open('./datasynopsis/ROI_' + str(row[6]) + '_' + str(row[5]) + '.jpg')
		if((data[i][0] == data[i-1][0]) and (aInRangebc(data[i-1][2],data[i][2],row[0]) or aInRangebc(data[i-1][2],row[0],data[i][2]) or aInRangebc(data[i-1][1],data[i][1],row[1]) or aInRangebc(data[i-1][1],row[1],data[i][1]))):
			if((aInRangebc(row[0],data[i-1][2],data[i-1][4]) and aInRangebc(row[1],data[i-1][1],data[i-1][3])) or (aInRangebc(row[2],data[i-1][2],data[i-1][4]) and aInRangebc(row[1],data[i-1][1],data[i-1][3])) or (aInRangebc(row[2],data[i-1][2],data[i-1][4]) and aInRangebc(row[3],data[i-1][1],data[i-1][3])) or (aInRangebc(row[0],data[i-1][2],data[i-1][4]) and aInRangebc(row[3],data[i-1][1],data[i-1][3])) or      (aInRangebc(data[i-1][2],row[0],row[2]) and aInRangebc(data[i-1][1],row[1],row[3])) or (aInRangebc(data[i-1][4],row[0],row[2]) and aInRangebc(data[i-1][1],row[1],row[3])) or (aInRangebc(data[i-1][4],row[0],row[2]) and aInRangebc(data[i-1][3],row[1],row[3])) or (aInRangebc(data[i-1][2],row[0],row[2]) and aInRangebc(data[i-1][3],row[1],row[3]))):
				im2.putalpha(80)
				im1.paste(im2, (int(row[0]), int(row[1])), im2)
				k = 1
			else:
				if(k == 2):
					im2.putalpha(80)
					im1.paste(im2, (int(row[0]), int(row[1])), im2)
				else:
					im1.paste(im2, (int(row[0]), int(row[1])))
		elif((data[i][0] == data[i+1][0]) and (((data[i+1][2] >= data[i][2]) and (data[i+1][2] <= row[0])) or ((data[i+1][2] <= data[i][2]) and (data[i+1][2] >= row[0])) or ((data[i+1][1] >= data[i][1]) and (data[i+1][1] <= row[1])) or ((data[i+1][1] <= data[i][1]) and (data[i+1][1] >= row[1])))):
			if((aInRangebc(row[0],data[i+1][2],data[i+1][4]) and aInRangebc(row[1],data[i+1][1],data[i+1][3])) or (aInRangebc(row[2],data[i+1][2],data[i+1][4]) and aInRangebc(row[1],data[i+1][1],data[i+1][3])) or (aInRangebc(row[2],data[i+1][2],data[i+1][4]) and aInRangebc(row[3],data[i+1][1],data[i+1][3])) or (aInRangebc(row[0],data[i+1][2],data[i+1][4]) and aInRangebc(row[3],data[i+1][1],data[i+1][3])) or      (aInRangebc(data[i+1][2],row[0],row[2]) and aInRangebc(data[i+1][1],row[1],row[3])) or (aInRangebc(data[i+1][4],row[0],row[2]) and aInRangebc(data[i+1][1],row[1],row[3])) or (aInRangebc(data[i+1][4],row[0],row[2]) and aInRangebc(data[i+1][3],row[1],row[3])) or (aInRangebc(data[i+1][2],row[0],row[2]) and aInRangebc(data[i+1][3],row[1],row[3]))):
				im2.putalpha(80)
				im1.paste(im2, (int(row[0]), int(row[1])), im2)
				k = 2
			else:
				if(k == 1):
					im2.putalpha(80)
					im1.paste(im2, (int(row[0]), int(row[1])), im2)
				else:
					im1.paste(im2, (int(row[0]), int(row[1])))
		else:
			if((aInRangebc(row[0],data[i][2],data[i][4]) and aInRangebc(row[1],data[i][1],data[i][3])) or (aInRangebc(row[2],data[i][2],data[i][4]) and aInRangebc(row[1],data[i][1],data[i][3])) or (aInRangebc(row[2],data[i][2],data[i][4]) and aInRangebc(row[3],data[i][1],data[i][3])) or (aInRangebc(row[0],data[i][2],data[i][4]) and aInRangebc(row[3],data[i][1],data[i][3])) or      (aInRangebc(data[i][2],row[0],row[2]) and aInRangebc(data[i][1],row[1],row[3])) or (aInRangebc(data[i][4],row[0],row[2]) and aInRangebc(data[i][1],row[1],row[3])) or (aInRangebc(data[i][4],row[0],row[2]) and aInRangebc(data[i][3],row[1],row[3])) or (aInRangebc(data[i][2],row[0],row[2]) and aInRangebc(data[i][3],row[1],row[3]))):
				im2.putalpha(80)
				im1.paste(im2, (int(row[0]), int(row[1])), im2)
			else:
				im1.paste(im2, (int(row[0]), int(row[1])))
		im1.save('./datasynopsis2/ROI_' + str(data[i][0]) + '.jpg', quality=95)
		plot(row[0], row[1], row[2], row[3], row[4], row[5], data[i][0], row[7])
		if(i >= j):
			i = 0
		else:
			i = i + 1
print("===> Synopsis video")
