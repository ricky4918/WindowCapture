import cv2
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel
import pandas as pd



img = cv2.imread('Capture_nor_5300.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = img.reshape(-1)
df = pd.DataFrame()
df['Original Image'] = img2

gaussian_img = nd.gaussian_filter(img, sigma=3)
gaussian_img1 = gaussian_img.reshape(-1)
df['Gaussian s3'] = gaussian_img1


print(df)
cv2.imshow('Original Image', img)
cv2.imshow('gaussian', gaussian_img)
cv2.waitKey()
cv2.destroyAllWindows()