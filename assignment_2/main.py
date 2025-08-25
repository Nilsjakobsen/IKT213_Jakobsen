import matplotlib.pyplot as plt
import cv2






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
    emptyPictureArray = [:]
    height, width, channels = image.shape
    height=
    width=
    channels=

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




cv2.imwrite("solutions/lena_copy.png",    )

if __name__ ==  "__main__":
    main()


