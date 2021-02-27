#Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

#Importing libraries necessary for Gaussian Smoothing
from scipy import ndimage

#Reading given image ("Brain.jpg") into array
img_array=plt.imread("Brain.jpg")
plt.imshow(img_array)
plt.show()

#Finding dimensions(shape) of image read into array
img_array.shape

#Plotting Histogram of the original image
plt.hist(img_array, bins=10)
plt.title("Original Image")
plt.show()

#Viewing the original image in Reverse Grayscale and saving the image on the hard disk.
plt.imshow(img_array, cmap='Greys_r')
plt.show()

#Performing Gaussian Filtering with sigma = 5
sigma_05 = ndimage.gaussian_filter(img_array, sigma = 5)
plt.imshow(sigma_05, cmap='Greys_r')
plt.show()

#Plotting the respective histogram
plt.hist(sigma_05, bins=10)
plt.title("Sigma = 5")
plt.show()

#Performing Gaussian Filtering with sigma = 10
sigma_10 = ndimage.gaussian_filter(img_array, sigma = 10)
plt.imshow(sigma_10, cmap='Greys_r')
plt.show()

#Plotting the respective histogram
plt.hist(sigma_10, bins=10)
plt.title("Sigma = 10")
plt.show()

#Performing Gaussian Filtering with sigma = 20
sigma_20 = ndimage.gaussian_filter(img_array, sigma = 20)
plt.imshow(sigma_20, cmap='Greys_r')
plt.show()

#Plotting the respective histogram
plt.hist(sigma_20, bins=10)
plt.title("Sigma = 20")
plt.show()

#Performing Gaussian Filtering with sigma = 30
sigma_30 = ndimage.gaussian_filter(img_array, sigma = 30)
plt.imshow(sigma_30, cmap='Greys_r')
plt.show()


#Plotting the respective histogram
plt.hist(sigma_30, bins=10)
plt.title("Sigma = 30")
plt.show()

#Performing Gaussian Filtering with sigma = 40
sigma_40 = ndimage.gaussian_filter(img_array, sigma = 40)
plt.imshow(sigma_40, cmap='Greys_r')
plt.show()

#Plotting the respective histogram
plt.hist(sigma_40, bins=10)
plt.title("Sigma = 40")
plt.show()

#Performing Gaussian Filtering with sigma = 50
sigma_50 = ndimage.gaussian_filter(img_array, sigma = 50)
plt.imshow(sigma_50, cmap='Greys_r')
plt.show()

#Plotting the respective histogram
plt.hist(sigma_50, bins=10)
plt.title("Sigma = 50")
plt.show()
