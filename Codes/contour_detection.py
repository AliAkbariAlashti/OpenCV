import cv2

# Detecting contours in the image
img = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("nothing found!!!")
    exit()

# Threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find Contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Drawing contours on the original image
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(img_color, contours, -1, (0, 255, 0), 2)

# Show and Save the result
cv2.imshow('Contours', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('contours.jpg', img_color)
