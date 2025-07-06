import cv2

img = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("nothing found!!!")
    exit()

# Threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive Threshold
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# save and show the result
cv2.imshow('Simple Threshold', thresh)
cv2.imshow('Adaptive Threshold', adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('simple_threshold.jpg', thresh)
cv2.imwrite('adaptive_threshold.jpg', adaptive)