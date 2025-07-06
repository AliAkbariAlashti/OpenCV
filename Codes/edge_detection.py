import cv2

# Edge detection with Canny algorithm
img = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("nothing found!!!")
    exit()

# Canny
edges = cv2.Canny(img, 100, 200)

# show the result
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save the result
cv2.imwrite('edges.jpg', edges)