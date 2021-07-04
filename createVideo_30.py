import cv2
import numpy as np
import glob, os
from natsort import natsorted

def CreateVideo_30(fps):
	print("Creating Video...")
	img_array = []
	n= 0
	dataset_path = "/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynopsis12"
	# # print(glob.glob('/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynoSpsis/*.jpg', recursive=True))
	img0 = cv2.imread("./datasynopsis11/IBG.jpg")
	height0, width0, layers0 = img0.shape
	size0 = (width0,height0)
	out = cv2.VideoWriter('./video/project3.avi',cv2.VideoWriter_fourcc(*'mp4v'), fps, size0)
	for filename in natsorted(glob.iglob(os.path.join(dataset_path, "*.jpg"))):
	    img = cv2.imread(filename)
	    # cv2.imshow('adf',img)
	    # cv2.waitKey()
	    height, width, layers = img.shape
	    size = (width,height)
	    # img_array.append(img)
	    out.write(img)


	 
	# for i in range(len(img_array)):
	#     out.write(img_array[i])
	cv2.destroyAllWindows()
	out.release()		
	print("Done!")

# from PIL import Image, ImageDraw, ImageFilter
# from utils.plots import plot_one_box
# import cv2
# # import Image

# # def trans_paste(fg_img,bg_img,alpha=1.0,box=(0,0)):
# #     fg_img_trans = Image.new("RGBA",fg_img.size)
# #     fg_img_trans = Image.blend(fg_img_trans,fg_img,alpha)
# #     bg_img.paste(fg_img_trans,box,fg_img_trans)
# #     return bg_img

# im1 = Image.open('./datasynopsis1/frame0.jpg')
# im2 = Image.open('./datasynopsis/ROI_1675_0.jpg')
# im3 = Image.open('./datasynopsis/ROI_248_0.jpg')
# # im2.putalpha(128)
# im1.paste(im2, (39, 153))
# print(im2.layers)
# im3.putalpha(80)
# im1.paste(im3, (63, 167), im3)
# print(im1.layers)
# # p = trans_paste(im1,im2,(39, 153))
# im1.show()
# # im1.save('./datasynopsis4/ROI_1675_0.jpg', quality=95)

# # img0 = cv2.imread('./datasynopsis2/ROI_1675_0.jpg')
# # xyxy = [39, 153, 97, 264]
# # classes = "person"
# # time =  '  ' + '1:51.30'
# # label = f'{classes} {time}'
# # plot_one_box(xyxy, img0, label=label, color=(255, 0, 0) , line_thickness=1)
# # cv2.imwrite('./datasynopsis2/ROI_1675_0.jpg', img0)

