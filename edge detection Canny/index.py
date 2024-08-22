import cv2 as cv
import matplotlib.pyplot as plt

#define a var for image read
image = cv.imread("image.jpg", cv.IMREAD_GRAYSCALE)

#edge detection use canny alghoritms
edge = cv.Canny(image, 150, 200)

#shows edge detection
# - close the current plot
plt.close()

# - create subplots the 1 area
# 121 => 1. environment - 2. divition - 1. one th area
plt.subplot(121)

# choice the title for plots
plt.title("Orginal Image")

# shows plt
# cmap = 'gray' => this images for reads a grayscale also print grayscale
plt.imshow(image, cmap='gray')

# hide the axis for plt
plt.axis("off")

# - create subplots the 1 area
# 121 => 1. environment - 2. divition - 2. one th area
plt.subplot(122)

# choice the title for plots
plt.title("Edges Image")

# shows plt
# cmap = 'gray' => this images for reads a grayscale also print grayscale
plt.imshow(edge, cmap='gray')

# hide the axis for plt
plt.axis("off")

plt.show()