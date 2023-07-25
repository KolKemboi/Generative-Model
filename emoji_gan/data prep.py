import cv2 
import os
import shutil
from time import sleep

fold_path = "C:\\Users\\USER\\Documents\\datasets\\emoji dataset"

files = os.listdir(fold_path)

for file in files:
	image = cv2.imread(os.path.join(fold_path, file))
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	reshaped_image = cv2.resize(gray_image, (28, 28))
	cv2.imshow("image", reshaped_image)
	print(reshaped_image.shape)
	cv2.waitKey(0)
	

cv2.destroyAllWindows()
