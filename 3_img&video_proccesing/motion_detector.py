import cv2
import time



video = cv2.VideoCapture(0) #0 is by default the webcam, then 1 2 m3 for others cameras connected.

while True:

    check, frame = video.read()

    gray_frame = cv2.cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray_frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows