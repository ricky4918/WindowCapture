from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time


New_window = {'top': 200, 'left': 300, 'width': 640, 'height': 480 }
sct = mss()

#Capture dark image

# input('Please Cover lens & press any button to capture the dark image')
# sct_img = sct.grab(New_window)
# img = Image.frombytes('RGB', (sct_img.size.width, sct_img.height), sct_img.rgb)
# img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
# cv2.imwrite(r'C:\Users\rebec\Desktop\WindowCapture\dark_image.bmp', np.array(img_gray))
# print('image is captured')
# input('press any button')
img_drk = cv2.imread('dark_image.bmp', 0)
#img_drk2 = cv2.imread('dark_image2.bmp',0)


while 1:
    begin_time = time()
    sct_img = sct.grab(New_window)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.height), sct_img.rgb)
    img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)


    img_blc = cv2.subtract(img_gray, img_drk)
    #img_blc2 = cv2.subtract(img_gray, img_drk2)
    #img_blc_both = cv2.subtract(img_blc, img_blc2)
    img_median = cv2.medianBlur(img_blc, 5)

    #img_blur = cv2.blur(img_blc, (3,3))
    img_norm = cv2.normalize(img_median, None, 0, 255, cv2.NORM_MINMAX )
    cv2.imshow('blc', np.array(img_blc))
    #cv2.imshow('blc2', np.array(img_blc2))
    #cv2.imshow('img_blc_both', np.array(img_blc_both))
    cv2.imshow('Normalized', np.array(img_norm))
    cv2.imshow('Median', np.array(img_median))
    #cv2.imshow('blur', np.array(img_blur))
    ms = 1000 * (time() - begin_time)
    #print("This frame rate: {} FPS.".format(1000//ms))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break