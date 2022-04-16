# import os
# import cv2
# from matplotlib import pyplot as plt
import numpy as np
import math
# import sys

# Interpolation kernel
def u(s, a):
    if (abs(s) >= 0) & (abs(s) <= 1):
        return (a + 2) * (abs(s) ** 3) - (a + 3) * (abs(s) ** 2) + 1
    elif (abs(s) > 1) & (abs(s) <= 2):
        return a * (abs(s) ** 3) - (5 * a) * (abs(s) ** 2) + (8 * a) * abs(s) - 4 * a
    return 0


# Padding to fit the model for bicubic interpolation
def padding(img, H, W, C):
    zimg = np.zeros((H + 4, W + 4, C))

    # Copying our original image to the middle of the padded image
    zimg[2 : H + 2, 2 : W + 2, :C] = img

    # Padding the first two col and row
    zimg[2 : H + 2, 0:2, :C] = img[:, 0:1, :C]
    zimg[H + 2 : H + 4, 2 : W + 2, :] = img[H - 1 : H, :, :]

    # Padding the last two col and row
    zimg[2 : H + 2, W + 2 : W + 4, :] = img[:, W - 1 : W, :]
    zimg[0:2, 2 : W + 2, :C] = img[0:1, :, :C]

    # Pad the missing eight points in the eight corners
    zimg[0:2, 0:2, :C] = img[0, 0, :C]
    zimg[H + 2 : H + 4, 0:2, :C] = img[H - 1, 0, :C]
    zimg[H + 2 : H + 4, W + 2 : W + 4, :C] = img[H - 1, W - 1, :C]
    zimg[0:2, W + 2 : W + 4, :C] = img[0, W - 1, :C]

    return zimg


# TEMPLATE FOR PROGRESS BAR
# def get_progressbar_str(progress):
#     END = 170
#     MAX_LEN = 30
#     BAR_LEN = int(MAX_LEN * progress)
#     return (
#         "Progress:["
#         + "=" * BAR_LEN
#         + (">" if BAR_LEN < MAX_LEN else "")
#         + " " * (MAX_LEN - BAR_LEN)
#         + "] %.1f%%" % (progress * 100.0)
#     )


# Bicubic operation
def bicubic(img, new_h, new_w, a):
    # Get image size
    old_h, old_w, C = img.shape

    img = padding(img, old_h, old_w, C)
    # Create new image

    dst = np.zeros((new_h, new_w, 3))

    # print(dst.shape)

    w_scale_factor = old_w / new_w
    h_scale_factor = old_h / new_h

    # print("Start bicubic interpolation")
    # print("It will take a little while...")
    # inc = 0
    for c in range(C):
        for j in range(new_h):
            for i in range(new_w):
                x, y = i * w_scale_factor + 2, j * h_scale_factor + 2

                x1 = 1 + x - math.floor(x)
                x2 = x - math.floor(x)
                x3 = math.floor(x) + 1 - x
                x4 = math.floor(x) + 2 - x

                y1 = 1 + y - math.floor(y)
                y2 = y - math.floor(y)
                y3 = math.floor(y) + 1 - y
                y4 = math.floor(y) + 2 - y

                mat_l = np.matrix([[u(x1, a), u(x2, a), u(x3, a), u(x4, a)]])
                mat_m = np.matrix(
                    [
                        [
                            img[int(y - y1), int(x - x1), c],
                            img[int(y - y2), int(x - x1), c],
                            img[int(y + y3), int(x - x1), c],
                            img[int(y + y4), int(x - x1), c],
                        ],
                        [
                            img[int(y - y1), int(x - x2), c],
                            img[int(y - y2), int(x - x2), c],
                            img[int(y + y3), int(x - x2), c],
                            img[int(y + y4), int(x - x2), c],
                        ],
                        [
                            img[int(y - y1), int(x + x3), c],
                            img[int(y - y2), int(x + x3), c],
                            img[int(y + y3), int(x + x3), c],
                            img[int(y + y4), int(x + x3), c],
                        ],
                        [
                            img[int(y - y1), int(x + x4), c],
                            img[int(y - y2), int(x + x4), c],
                            img[int(y + y3), int(x + x4), c],
                            img[int(y + y4), int(x + x4), c],
                        ],
                    ]
                )
                mat_r = np.matrix([[u(y1, a)], [u(y2, a)], [u(y3, a)], [u(y4, a)]])
                dst[j, i, c] = np.dot(np.dot(mat_l, mat_m), mat_r)
                # print(dst[j,i,c])

                # Print progress
                # inc = inc + 1
                # sys.stderr.write(
                #     "\r\033[K" + get_progressbar_str(inc / (C * new_h * new_w))
                # )
                # sys.stderr.flush()
    # sys.stderr.write("\n")
    # sys.stderr.flush()
    return dst.astype(int) # correct


# def main():
#     # image path depending on the system
#     img = cv2.imread(
#         "/Users/apple/image_interpolation_algos/image_interpolation/images/image1.jpg"
# )

#     # Aspect ratio of our image
#     aspect_ratio = img.shape[0] / img.shape[1]

#     # play with the new width here
#     new_width = 400

#     # get the billinear interpolated image here
#     new_img = bicubic(img, int(new_width * aspect_ratio), new_width, -1 / 2)
#     print(new_img.shape)

#     # plotting for difference in image view

#     fig = plt.figure(figsize=(100, 7))
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
#     plt.show()

# if __name__ == "__main__":
#     main()
