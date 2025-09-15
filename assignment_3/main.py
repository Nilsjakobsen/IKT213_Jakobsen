import cv2
import numpy as np
from pathlib import Path




def sobel_edge_detection(image):

    img_blur = cv2.GaussianBlur(image, (3, 3), sigmaX=0)
    sobelxy = cv2.Sobel(img_blur, cv2.CV_64F, dx=1, dy=1, ksize=1)
    return sobelxy



def canny_edge_detection(image, threshold_1, threshold_2):
    edges = cv2.Canny(image, threshold_1, threshold_2)


    return edges

def template_match(image, template):

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    out = image.copy()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(out, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return out

def resize(image, scale_factor: int, up_or_down: str):


    if up_or_down.lower ()== "up":
        return cv2.pyrUp(image)
    elif up_or_down.lower()== "down" :
        return cv2.pyrDown( image)
    else:
        return image


def main():
    #task 1
    img =cv2.imread("lambo.png")
    edge = sobel_edge_detection(img)
    cv2.imwrite("solutions/sobel.png", edge)
    #task 2
    canny = canny_edge_detection(img, 50,50)
    cv2.imwrite("solutions/Canny.png", canny)
    #task 3

    shape = cv2.imread("shapes-1.png")
    template = cv2.imread("shapes_template.jpg")
    matched = template_match(shape,template)
    cv2.imwrite("solutions/template_match.png", matched)

    #task 4
    win ="lambo"
    src = cv2.imread("lambo.png")
    cv2.namedWindow(win, cv2.WINDOW_AUTOSIZE)
    while   True:
        if  cv2.getWindowProperty(win,  cv2.WND_PROP_VISIBLE)  < 1:
            break
        cv2.imshow("lambo",src)
        k =cv2.waitKey(0)
        if k ==27:
            break
        elif   k == ord("i"):
            src=resize(src,2,"up")
        elif  k== ord("o"):
            src = resize(src,2,"down")

    cv2.imwrite("solutions/resizedlambo.png",  src)
    cv2.destroyAllWindows()


if __name__ ==  "__main__":
    main()