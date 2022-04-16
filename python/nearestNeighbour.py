# import cv2
import math
import numpy as np
# import os
# import matplotlib.pyplot as plt
import copy

def nearest_neighbour(img, new_h, new_w):
	old_h, old_w, c = img.shape
	resized = np.zeros((new_h, new_w, c))
	w_scale_factor = (old_w ) / (new_w ) if new_h != 0 else 0
	h_scale_factor = (old_h ) / (new_h ) if new_w != 0 else 0
	for i in range(new_h):
		for j in range(new_w):
			x = i * h_scale_factor
			y = j * w_scale_factor

			x_floor = math.floor(x)
			# x_ceil = min( old_h - 1, math.ceil(x))
			y_floor = math.floor(y)
			# y_ceil = min(old_w - 1, math.ceil(y))

			resized[i,j,:] = copy.deepcopy(img[x_floor, y_floor,:])
	return resized.astype(np.uint8)


# def main():
# 	# image path depending on the system
# 	img=cv2.imread(os.getcwd() + '/image_interpolation/src/main/python/testImages/example.jpg')
# 	print(img.shape)
# 	# Aspect ratio of our image
# 	aspect_ratio = img.shape[0] / img.shape[1]

# 	# play with the new width here
# 	new_width = 900

# 	# get the billinear interpolated image here
# 	new_img=nearest_neighbour(img,int(new_width * aspect_ratio),new_width)
# 	print(new_img.shape)
# 	# plotting for difference in image view
# 	fig = plt.figure(figsize=(100, 7))
# 	rows = 1
# 	columns = 2
# 	fig.add_subplot(rows, columns, 1)
# 	plt.imshow(img)
# 	plt.axis('off')
# 	plt.title("Original" +" Dimensions: " + str(img.shape[0]) + "*" + str(img.shape[1]))
# 	fig.add_subplot(rows, columns, 2)
# 	plt.imshow(new_img)
# 	plt.axis('off')
# 	plt.title("Upscaled" +" Dimensions: " + str(new_img.shape[0]) + "*" + str(new_img.shape[1]))
# 	plt.show()


# if __name__ == "__main__":
# 	main()