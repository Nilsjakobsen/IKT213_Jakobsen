import cv2
import numpy as np

def print_image_information(image ):

    height,width,channels = image.shape


    print("height", height)
    print("width",width)
    print("channels",channels)
    print("size",image.size)
    print("data type",image.dtype)
    pass



def camera_info_save():
    cam= cv2.VideoCapture(0)
    fps =cam.get(cv2.CAP_PROP_FPS)
    width =cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

    with open("solutions/camera_outputs.txt","w") as f:
        f.write(f"fps: {fps}\n")
        f.write(f"width: {width}\n")
        f.write(f"height: {height}\n")
        cam.release()
def main():

    img =cv2.imread("lena.png")
    cv2.imshow("image",img)
    cv2.waitKey(0)
    print_image_information(img)
    camera_info_save()
    print("camera info saved")
if __name__ ==  "__main__":
    main()