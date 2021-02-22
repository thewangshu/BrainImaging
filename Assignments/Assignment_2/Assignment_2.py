#Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

#Importing libraries necessary for Gaussian Smoothing
from scipy import misc,ndimage

#Reading given image ("Brain.jpg") into array
img_array=plt.imread("Brain.jpg")
plt.imshow(img_array)
plt.show()

#Finding dimensions(shape) of image read into array
img_array.shape

#Correcting Image by viewing it in Reverse Grayscale and saving it as ReverseGS_Brain.png
plt.imshow(img_array, cmap='Greys_r')
plt.show()

#Plotting Histogram of Reverse_GS.png
plt.hist(img_array, bins=10)

#Performing Gaussian Filtering with sigma = 5 and plotting a histogram of the same
sigma_05 = ndimage.gaussian_filter(img_array, sigma = 5)
plt.imshow(sigma_05)
plt.show()
plt.hist(sigma_05, bins=10)

#Performing Gaussian Filtering with sigma = 10 and plotting a histogram of the same
sigma_10 = ndimage.gaussian_filter(img_array, sigma = 10)
plt.imshow(sigma_10)
plt.show()
plt.hist(sigma_10, bins=10)

#Performing Gaussian Filtering with sigma = 20 and plotting a histogram of the same
sigma_20 = ndimage.gaussian_filter(img_array, sigma = 20)
plt.imshow(sigma_20)
plt.show()
plt.hist(sigma_20, bins=10)

#Performing Gaussian Filtering with sigma = 30 and plotting a histogram of the same
sigma_30 = ndimage.gaussian_filter(img_array, sigma = 30)
plt.imshow(sigma_30)
plt.show()
plt.hist(sigma_30, bins=10)

#Performing Gaussian Filtering with sigma = 40 and plotting a histogram of the same
sigma_40 = ndimage.gaussian_filter(img_array, sigma = 40)
plt.imshow(sigma_40)
plt.show()
plt.hist(sigma_40, bins=10)

#Performing Gaussian Filtering with sigma = 50 and plotting a histogram of the same
sigma_50 = ndimage.gaussian_filter(img_array, sigma = 50)
plt.imshow(sigma_50)
plt.show()
plt.hist(sigma_50, bins=10)
