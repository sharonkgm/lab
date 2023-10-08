import cv2 

image1 = cv2.imread(r'2nd sem\DIP\messi1.jpg')
image2=cv2.imread(r'2nd sem\DIP\messi2.jpg')
added_images = cv2.add(image1,image2)
cv2.imshow('image', added_images)
cv2.waitKey(0)
cv2.distroyAllWindows()