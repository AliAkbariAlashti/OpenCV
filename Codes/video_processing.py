import cv2

# Video proccesing and Gray 
cap = cv2.VideoCapture('sample_video.mp4')
if not cap.isOpened():
    print("nothing found!!!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Frame to Gry
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Frame show 
    cv2.imshow('Video', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
