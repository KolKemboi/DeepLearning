import cv2
import os
import pathlib
import sys

DIR = "data"
files = os.listdir(DIR) 
folders = "allo,john,kenna,kevo,ndichu".split(",")

"""
for file in folders:
	if (os.path.exists(os.path.join(DIR, file))):
		os.mkdir(os.path.join(DIR, file.split("_")[0]))
	else:
		os.mkdir(os.path.join(DIR, file.split("_")[0]))

"""
print(files)
counter = 0

for file in files:


	if "mp4" in file:
		vid = cv2.VideoCapture(os.path.join(DIR, file))
	else:
		continue
	file_num = 0

	while True:
		ret, frame = vid.read()

		if ret == True:
			image_name = file.split('_')[0]
			image_file_name = f"{image_name}_{file_num}.jpg"

			print(image_file_name)
			frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)

			gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			cv2.imshow("frame", gray_image)
			file_num += 1

			image_path = os.path.join(DIR,image_name,image_file_name)
			cv2.imwrite(image_path, gray_image)
			
			

		if cv2.waitKey(1) & 0xFF == ord("q") or ret == False:
			break

	
cv2.destroyAllWindows()
