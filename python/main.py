# THIS WILL BE THE ENTRY POINT FOR THE INTERPOLATION OF THE IMAGE USING PYTHON

# FROM HERE WE WILL CALL THE DIFFERENT INTERPOLATION ALGORITHMS USING THE FLAGS SPECIFIED
# DURING THE CALLING OF PYTHON COMMAND USING JAVA
import sys
import cv2
import os


import nearestNeighbour, billinear , bicubic , idw

# print("Hello World")

algoToExecute = sys.argv[1]

scalingVal = int(sys.argv[2])

fileName = sys.argv[3]

isJpg = fileName.find(".")
isJpg = fileName[isJpg:]
if (fileName == "jpg" or fileName == "jpeg"):
	isJpg = True
else:
	isJpg = False

# multiplicativeFactor = sys.argv[2]
# print(algoToExecute)
# print("Hello World")

img = cv2.imread(os.path.join(os.getcwd() , "images", fileName))

# print(img.shape)
# Aspect ratio of our image
# aspect_ratio = img.shape[0] / img.shape[1]

old_height = img.shape[0]
old_width = img.shape[1]

# print(algoToExecute)

# play with the new width here


if(algoToExecute == "nearest_neighbour"):  
    # print(algoToExecute + "")
    img = nearestNeighbour.nearest_neighbour(img, scalingVal * old_height , scalingVal * old_width)
    cv2.imwrite(os.path.join(os.getcwd(),"images" , "processedImage") + (".jpg" if isJpg else ".png"),img)
elif(algoToExecute == "bilinear"):
	img = billinear.billinear(img, scalingVal * old_height , scalingVal * old_width)
	cv2.imwrite(os.path.join(os.getcwd(),"images" , "processedImage") + (".jpg" if isJpg else ".png") ,img)
elif(algoToExecute == "bicubic"):
	img = bicubic.bicubic(img, scalingVal * old_height , scalingVal * old_width , -1 / 2)
	cv2.imwrite(os.path.join(os.getcwd(),"images" , "processedImage") + (".jpg" if isJpg else ".png"),img)
elif(algoToExecute == "idw"):
	img = idw.idw(img, scalingVal * old_height , scalingVal * old_width)
	cv2.imwrite(os.path.join(os.getcwd(),"images" , "processedImage") + (".jpg" if isJpg else ".png"),img)
else:
	pass
