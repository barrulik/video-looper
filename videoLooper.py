# Python program to play a video
# in reverse mode using opencv

# import cv2 library
import cv2
import os
import shutil

if os.path.isdir("images"):
	shutil.rmtree("images")
os.mkdir("images")
fileName = input("type the file path: ")
# videoCapture method of cv2 return video object
# Pass absolute address of video file
cap = cv2.VideoCapture(fileName)

# remove extention from file
while (fileName[len(fileName)-1] != "."):
	fileName = fileName[:-1]
fileName = fileName[:-1]

# read method of video object will return
# a tuple with 1st element denotes whether
# the frame was read successfully or not,
# 2nd element is the actual frame.

# Grab the current frame.
check , vid = cap.read()

# counter variable for
# counting frames
counter = 0

# Initialize the value
# of check variable
check = True

frame_list = []

# If reached the end of the video
# then we got False value of check.

# keep looping until we
# got False value of check.
while(check == True):
	
	# imwrite method of cv2 saves the
	# image to the specified format.
	cv2.imwrite("./images/frame%d.jpg" %counter , vid)
	check , vid = cap.read()
	
	

	# Add each frame in the list by
	# using append method of the List
	frame_list.append(vid)
	
	# increment the counter by 1
	counter += 1

# last value in the frame_list is None
# because when video reaches to the end
# then false value store in check variable
# and None value is store in vide variable.

# removing the last value from the
# frame_list by using pop method of List
frame_list.pop()
new_frame_list = frame_list.copy()
new_frame_list.reverse()
frame_list = frame_list+new_frame_list
# make it all into a vid


img = cv2.imread("./images/frame0.jpg")
height, width, layers = img.shape
size = (width,height)

out = cv2.VideoWriter(fileName + '_result.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 60,size)
 
for i in range(len(frame_list)):
    out.write(frame_list[i])
out.release()
print("done")
