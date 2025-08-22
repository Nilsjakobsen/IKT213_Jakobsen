import cv2
import numpy as np
def print_image_information(image ):

    width,height,channels = image.shape


    print("height", height)
    print("width",width)
    print("channels",channels)
    print("size",image.size)
    print("data type",image.dtype)
    pass

def main():

    img =cv2.imread("lena.png")
    cv2.imshow("image",img)
    cv2.waitKey(0)
    print_image_information(img)

if __name__ ==  "__main__":
    main()