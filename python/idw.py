import math
# from cv2 import imwrite
import numpy as np

# import cv2
# import matplotlib.pyplot as plt



def padding(img, H, W, C):
    zimg = np.zeros((H + 6, W + 6, C))

    # Copying our original image to the middle of the padded image
    zimg[3 : H + 3, 3 : W + 3, :C] = img

    # Padding the first two col and row
    zimg[3 : H + 3, 0:3, :C] = img[:, 0:1, :C]
    zimg[H + 3 : H + 6, 3 : W + 3, :] = img[H - 1 : H, :, :]

    # Padding the last two col and row
    zimg[3 : H + 3, W + 3 : W + 6, :] = img[:, W - 1 : W, :]
    zimg[0:3, 3 : W + 3, :C] = img[0:1, :, :C]

    # Pad the missing eight points in the eight corners
    zimg[0:3, 0:3, :C] = img[0, 0, :C]
    zimg[H + 3 : H + 6, 0:3, :C] = img[H - 1, 0, :C]
    zimg[H + 3 : H + 6, W + 3 : W + 6, :C] = img[H - 1, W - 1, :C]
    zimg[0:3, W + 3 : W + 6, :C] = img[0, W - 1, :C]

    return zimg


def inverseDist(x , y , currX , currY):
    return 1.0 / (math.sqrt((x - currX)**2 + (y - currY)**2)) ** 1.7


def idw(img, new_h, new_w):

    # height , width and channels for the orig image
    old_h, old_w, c = img.shape
    # padding our image for taking care of the corner pixels
    paddedImage = padding(img , old_h, old_w , c)

    # initializing the new image with the new dimensions
    newImg = np.zeros((new_h, new_w, c))

    # scale factor for the images
    w_scale_factor = (old_w ) / (new_w ) if new_h != 0 else 0
    h_scale_factor = (old_h ) / (new_h ) if new_w != 0 else 0


    for i in range(new_h):
        for j in range(new_w):
            x = i * h_scale_factor + 3
            # i = 2 , j = 3  , 0.3 ==== x = 0.6 , y = 0.9
            y = j * w_scale_factor + 3

            # setting the regions for the weighted average
            x_max_left = int(x - 3)
            x_max_right = int(x + 3) 
            y_max_top = int(y + 3)
            y_max_bottom = int(y - 3)

            # for the current pixel value finding the numerator and denominator
            numerator = 0.0
            denominator = 0.0

            # print(inverseDist(1 , 2 , 4 , 5))
            # print(x_max_left , x_max_right , y_max_bottom, y_max_top

            # finding the pixel value using the inverse weighted average algo
            for channel in range(c):
                numerator = 0.0
                denominator = 0.0
                for l in range(x_max_left , x_max_right + 1):
                    for m in range(y_max_bottom , y_max_top + 1):
                        if(x == l and m == y):
                            temp = 1
                        else:
                            temp = inverseDist(x - 3,y - 3 , l - 3 ,m - 3)
                        numerator = numerator + paddedImage[l][m][channel] * temp
                        denominator = denominator +  temp
                # print(numerator , denominator)
                # if denominator == 0:
                #     denominator = 1
                # print(np.divide(numerator , denominator).astype(np.uint8) )
                newImg[i,j,channel] = int(numerator / denominator)
    return newImg.astype(np.uint8)


# def main():
# 	# image path depending on the system
#     img=cv2.imread("/Users/apple/image_interpolation_algos/image_interpolation/images/teddyBear.jpeg")

# 	# Aspect ratio of our image
#     aspect_ratio = img.shape[0] / img.shape[1]

# 	# play with the new width here
#     new_width = 200

# 	# get the billinear interpolated image here
#     new_img=idw(img,int(new_width * aspect_ratio),new_width)
#     imwrite("/Users/apple/image_interpolation_algos/image_interpolation/images/newImg.jpg" , new_img)
#     # cv2.imshow("IMAGE",new_img)
# 	# plotting for difference in image view
#     """fig = plt.figure(figsize=(100, 7))
#     rows = 1
#     columns = 2
#     fig.add_subplot(rows, columns, 1)
#     plt.imshow(img)
#     plt.axis('off')
#     plt.title("Original" +" Dimensions: " + str(img.shape[0]) + "*" + str(img.shape[1]))
#     fig.add_subplot(rows, columns, 2)
#     plt.imshow(new_img)
#     plt.axis('off')
#     plt.title("Upscaled" +" Dimensions: " + str(new_img.shape[0]) + "*" + str(new_img.shape[1]))
#     plt.show()"""


# if __name__ == "__main__":
# 	main()