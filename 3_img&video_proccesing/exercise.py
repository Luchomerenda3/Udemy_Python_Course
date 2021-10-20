import cv2
import os


os.chdir("sample_images")

for file in os.listdir():
    aux_img = cv2.imwrite(file[:-4] + "_resized.jpg",cv2.resize(cv2.imread(file,1),(100,100)))

#solution given by the professor
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)