from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time


New_window = {'top': 30, 'left': 275, 'width': 760, 'height': 580 }
sct = mss()



while 1:
    begin_time = time()
    sct_img = sct.grab(New_window)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.height), sct_img.rgb)
    img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 5)
    inverted_image = cv2.bitwise_not(img_blur)
    edges = cv2.Canny(image=inverted_image, threshold1=20, threshold2=80) # Canny Edge Detection
    





    cv2.imshow('blc', np.array(inverted_image))
    cv2.imshow('Canny Edge Detection', edges)
    #cv2.imshow('Laplacian Edge Detection', laplacian)




    ms = 1000 * (time() - begin_time)
    #print("This frame rate: {} FPS.".format(1000//ms))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break