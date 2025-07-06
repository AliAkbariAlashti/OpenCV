import cv2

# Apply different filters to the image
img = cv2.imread('sample_image.jpg')
if img is None:
    print("nothing found!!!")
    exit()

# Gaussian Blur Filter
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur Filter
median = cv2.medianBlur(img, 5)

# show the result
cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', gaussian)
cv2.imshow('Median Blur', median)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save the result 
cv2.imwrite('gaussian_blur.jpg', gaussian)
cv2.imwrite('median_blur.jpg', median)