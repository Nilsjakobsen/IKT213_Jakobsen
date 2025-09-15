import cv2
import numpy as np
from pathlib import Path




def sobel_edge_detection(image):

    img_blur = cv2.GaussianBlur(image, (3, 3), sigmaX=0)
    sobelxy = cv2.Sobel(img_blur, cv2.CV_64F, dx=1, dy=1, ksize=1)
    return sobelxy



def canny_edge_detection(image, threshold_1, threshold_2)



    return
def main():

    img =cv2.imread("lambo.png")
    edge = sobel_edge_detection(img)
    cv2.imwrite("solutions/GaussianBlur.png", edge)
    print("camera info saved")
if __name__ ==  "__main__":
    main()