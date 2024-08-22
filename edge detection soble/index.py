import cv2 as cv
import matplotlib.pyplot as plt

#define a var for image read
image = cv.imread("image.jpg", cv.IMREAD_GRAYSCALE)

#edge detection use sobel alghoritms
sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, 3)
sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, 3)

# use magnitude method for combind sobelx and sobely
combind_edge = cv.magnitude(sobel_x, sobel_y)

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
plt.imshow(combind_edge, cmap='gray')

# hide the axis for plt
plt.axis("off")

plt.show()