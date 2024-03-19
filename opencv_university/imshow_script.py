import cv2
import matplotlib.pyplot as plt 
import os
import numpy as np
from IPython.display import Image

#read windows path

cb_img = cv2.imread('C:\\Users\pvesteban\github_repos\Curso-de-Computer-vision-y-Machine-Learning\opencv_university\checkerboard_color.png',1)
coke_img = cv2.imread('C:\\Users\pvesteban\github_repos\Curso-de-Computer-vision-y-Machine-Learning\opencv_university\coca-cola-logo.png', 1)

print("Checkerboard image shape:", cb_img.shape)
print("Coca-Cola logo image shape:", coke_img.shape)


#matplotlib inshow
plt.imshow(cb_img) #BGR
plt.title('Checkerboard | Matplotlib imshow')
plt.show()

#opencv imshow display for 8 seconds
window1 = cv2.namedWindow("W1")
cv2.imshow('W1', cb_img)
cv2.waitKey(8000)
cv2.destroyWindow('W1')

#opencv imshow display for 8 seconds for coke_img
window2 = cv2.namedWindow("W2")
cv2.imshow('W2', coke_img)
cv2.waitKey(8000)
cv2.destroyWindow('W2')

#opencv imshow display until key is pressed
window3 = cv2.namedWindow("W3")
cv2.imshow('W3', cb_img)
cv2.waitKey(0) #wait until any key is pressed
cv2.destroyWindow('W3')

