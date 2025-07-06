import cv2
import numpy as np

# Apply geometric transformations (rotation and scaling)
img = cv2.imread('sample_image.jpg')
if img is None:
    print("nothing found!!!")
    exit()

# image rotation
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

# image scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

# Show and Save 
cv2.imshow('Rotated', rotated)
cv2.imshow('Scaled', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('rotated.jpg', rotated)
cv2.imwrite('scaled.jpg', scaled)
