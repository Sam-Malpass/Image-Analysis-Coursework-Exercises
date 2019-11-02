# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:19:09 2019

@author: Sam
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_ubyte
from skimage.measure import compare_ssim

originalImage = cv.imread('PenguinOriginal.bmp',0)
noisyImage = cv.imread('PenguinNoise.bmp',0)

fig = plt.figure(figsize = (20, 35), dpi = 80, facecolor = 'w', edgecolor = 'k')
plt.subplot(121),plt.imshow(originalImage, cmap = 'gray')
plt.title('Orignal Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(noisyImage, cmap = 'gray')
plt.title('Noisy Image'), plt.xticks([]), plt.yticks([])
plt.show()

fig = plt.figure(figsize = (20, 10), dpi = 80, facecolor = 'w', edgecolor = 'k')
plt.subplot(121),plt.hist(originalImage.ravel(),256,[0,256])
plt.title('Orignal Image Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.hist(noisyImage.ravel(), 256, [0,256])
plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])
plt.show()