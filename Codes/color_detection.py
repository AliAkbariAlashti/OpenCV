import cv2
import numpy as np

# Detecting specific colors (e.g. red)
img = cv2.imread('sample_image.jpg')
if img is None:
    print("nothing found!!!")
    exit()

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the red color range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

# Show and Save the result
cv2.imshow('Red Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('red_mask.jpg', mask)