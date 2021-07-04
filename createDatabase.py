# import sqlite3
# import os
# os.remove("dtsynopsis.db")
# con = sqlite3.connect('dtsynopsis.db')
# cur = con.cursor()

# # Create table
# cur.execute('''CREATE TABLE stocks(x1 real, y1 real, x2 real, y2 real, time text, obj int, frame int, class text)''')


#-----------------------------------------------------------------------------------------------------------------
import sqlite3
import numpy as np

con = sqlite3.connect('dtsynopsis.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM stocks '):
	# print(type(row[4][2:7]))
	# data.append([row[3]-row[1], row[2] - row[0]])
	# print(row, float(row[4][0:1])*60 + float(row[4][2:7]))
	print(row)

# import cv2
# v = cv2.VideoCapture('0.mp4')
# b = v.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
# a = v.get(cv2.CAP_PROP_POS_MSEC)
# c = v.get(cv2.CAP_PROP_FRAME_COUNT)
# e = v.get(cv2.CAP_PROP_FPS) 
# print(a, b, c, round(e), e, 1/e)
# print(c/e/60)

# import cv2

# vod = cv2.VideoCapture('video6.mp4')

# ret, frame = vod.read()

# gpu_frame = cv2.cuda_GpuMat()

# while ret:
#     gpu_frame.upload(frame)

#     frame = cv2.cuda.resize(gpu_frame, (480, 852))
#     frame.download()

#     ret, frame = vod.read()
#----------------------------------------------- insert image
# import sqlite3
# import os
# os.remove("datasynopsis11.db")
# con = sqlite3.connect('datasynopsis11.db')
# cur = con.cursor()

# # Create table
# cur.execute('''CREATE TABLE stocks(id int, name text, photo blob)''')
# # CREATE TABLE new_employee ( id int, name text, photo blob);

# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         blobData = file.read()
#     return blobData

# def insertBLOB(empId, name, photo):
#     try:
#         sqliteConnection = sqlite3.connect('datasynopsis11.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")
#         sqlite_insert_blob_query = """ INSERT INTO stocks
#                                   (id, name, photo) VALUES (?, ?, ?)"""

#         empPhoto = convertToBinaryData(photo)
#         # resume = convertToBinaryData(resumeFile)
#         # Convert data into tuple format
#         data_tuple = (empId, name, empPhoto)
#         cursor.execute(sqlite_insert_blob_query, data_tuple)
#         sqliteConnection.commit()
#         print("Image inserted successfully as a BLOB into a table")
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to insert blob data into sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("the sqlite connection is closed")

# insertBLOB(1, "IBG", "/home/son/obdetect/OIDv4_ToolKit/yolov5/datasynopsis11/IBG.jpg")

#-------------------------------------------- Retrieve Image
# import sqlite3

# def writeTofile(data, filename):
#     # Convert binary data to proper format and write it on Hard Disk
#     with open(filename, 'wb') as file:
#         file.write(data)
#     print("Stored blob data into: ", filename, "\n")

# def readBlobData(empId):
#     try:
#         sqliteConnection = sqlite3.connect('datasynopsis12.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sql_fetch_blob_query = """SELECT * from stocks where id = ?"""
#         cursor.execute(sql_fetch_blob_query, (empId,))
#         record = cursor.fetchall()
#         for row in record:
#             print("Id = ", row[0], "Name = ", row[1])
#             name = row[1]
#             photo = row[2]

#             print("Storing employee image and resume on disk \n")
#             photoPath = "/home/son/obdetect/OIDv4_ToolKit/yolov5/" + name + ".jpg"
#             writeTofile(photo, photoPath)

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read blob data from sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("sqlite connection is closed")

# readBlobData(1)

# for i in range(10):
# 	for j in range(10):
# 		if(j<5):
# 			print("i=" + str(i))
# 		else:
# 			break
