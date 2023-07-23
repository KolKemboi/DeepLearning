import cv2
import os

filepath = "C:\\Users\\USER\\Documents\\datasets\\Face Dataset\\Face Dataset"

write_to = "C:\\Users\\USER\\Documents\\datasets\\Face Dataset"

folders = "allo,john,kenna,kevo,ndichu".split(",")

files = os.listdir(filepath)

for ind, file in enumerate(files):
	feed = cv2.VideoCapture(os.path.join(filepath, file))
	counter = 0

	while True:
		ret, frame = feed.read()

		if ret == True:

			counter += 1
			image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			image = cv2.resize(image, (0, 0), fx = 0.25, fy = 0.25)

			cv2.imshow("image", image)
			file_name = f"{file.split('.')[0]}_{counter}.jpg"

			save_path = os.path.join(write_to, file.split("_")[0],file_name)
			
			cv2.imwrite(save_path, image)

		if cv2.waitKey(1) & 0xFF == ord("q") or ret == False:
			break

cv2.destroyAllWindows()
