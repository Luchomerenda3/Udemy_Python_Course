import cv2

#1st lecture
#LEarning opencv library

img = cv2.imread("galaxy.jpg",0) #-1,0,1 depending on whether we want a coloured image or gray scaled image.

print(type(img))
print(img)
print(img.shape)

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resize an image

cv2.imshow("Galaxy",resized_image) #show an image
cv2.imwrite("Galaxy_resized.jpg",resized_image) #writing resized blcak & white image.
cv2.waitKey(0) #how the windows behaves
cv2.destroyAllWindows() #destroy the windows

#E


