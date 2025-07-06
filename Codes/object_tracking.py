import cv2

# Object tracking with KCF
cap = cv2.VideoCapture('sample_video.mp4')
if not cap.isOpened():
    print("nothing found!!!")
    exit()

# choosing the Frame to track 
ret, frame = cap.read()
bbox = cv2.selectROI('Select Object', frame, fromCenter=False)
tracker = cv2.TrackerKCF_create()
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Updating the tracker
    success, bbox = tracker.update(frame)
    if success:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Frame Show
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()