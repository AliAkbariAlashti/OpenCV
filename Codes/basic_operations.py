import cv2
import numpy as np

# Read, display and save
img = cv2.imread('sample_image.jpg')
if img is None:
    print("nothing found!!!")
    exit()

# Show the image 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image to GRY
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the image
cv2.imwrite('gray_image.jpg', gray)