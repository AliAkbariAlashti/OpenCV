import cv2

# Face recognition using Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('man_pic.jpg')
if img is None:
    print("nothing found!!!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# show and save the result
cv2.imshow('Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('faces_detected.jpg', img)