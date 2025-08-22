import cv2
import numpy as np
def print_image_information(image ):

    pass

def main():

    img =cv2.imread("lena.png")
    cv2.imshow("image",img)
    cv2.waitKey(0)

if __name__ ==  "__main__":
    main()