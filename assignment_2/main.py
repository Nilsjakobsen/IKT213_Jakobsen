import matplotlib.pyplot as plt
import cv2
import numpy as np


def padding(image, border_width):

    image_padded= cv2.copyMakeBorder( image, border_width,border_width,border_width,border_width,cv2.BORDER_REFLECT)

    return  image_padded

def crop(image, x_0,x_1,y_0,y_1):
    cropped_image = image[y_0:y_1, x_0:x_1]

    return cropped_image

def resize(image, width, height):
    resized_image = cv2.resize(image, (width,   height))

    return resized_image

def copy(image, emptyPictureArray):
    emptyPictureArray[:] =image
    return  emptyPictureArray

def grayscale(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def hsv(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def hue_shifted(image, emptyPictureArray, hue):

    image_shifted = np.clip(image.astype(np.int16)  + hue , 0 ,255) .astype(np.uint8)
    emptyPictureArray[:] = image_shifted
    return emptyPictureArray

def smoothing(image):
    return  cv2.GaussianBlur(image,(15, 15),0, borderType=cv2.BORDER_DEFAULT)

def rotation(image, rotation_angle):
    if rotation_angle == 90 :
        return cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

    elif rotation_angle==180:
        return cv2.rotate(image,cv2.ROTATE_180)



def main():
    img = cv2.imread("lena.png")
#task 1:
    border= padding(img,100)
    cv2.imwrite("solutions/lena_reflected.png",border)


#task 2:
    image_cropped= crop(img, 80, 512-130,80,512-130)
    cv2.imwrite("solutions/lena_cropped.png",image_cropped )

#task 3:
    resized =resize(img,200,200)
    cv2.imwrite("solutions/lena_resized.png",resized)

#task 4

    height,width,channels = img.shape

    emptyPictureArray=  np.zeros((height,width,3),dtype=img.dtype)
    image_copied= copy (img, emptyPictureArray)
    cv2.imwrite("solutions/lena_copy.png",image_copied    )


#task 5
    grayscaled= grayscale(img)

    cv2.imwrite("solutions/lena_grayscale.png", grayscaled  )



#task 6


    hsv1 = hsv(img)
    cv2.imwrite("solutions/lena_hsv.png", hsv1)

#task 7

    hue2 = np.zeros(( height,  width,3),  dtype=img.dtype)
    hue1 = hue_shifted(img, hue2, 50)
    cv2.imwrite("solutions/lena_hue.png", hue1 )

#task 8
    smooth= smoothing(img)
    cv2.imwrite("solutions/lena_smoothing.png",smooth )


#task 9
    rotated90= rotation(img,90)

    cv2.imwrite("solutions/lena_rotate90.png",rotated90  )

    rotated180= rotation(img,180)
    cv2.imwrite("solutions/lena_rotate180.png", rotated180)

if __name__ ==  "__main__":
    main()


