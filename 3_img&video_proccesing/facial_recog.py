import os
import cv2


os.chdir("Files")

#creating a cascade classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#open an image to check

img = cv2.imread("news.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=3,
                                      )

print(faces)

for x,y,w,h in faces:
    img_with_faces = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow("Faces",img_with_faces)
cv2.waitKey(0)
cv2.destroyAllWindows()







