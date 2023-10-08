import cv2
import numpy as np

image1 = cv2.imread(r'2nd sem\DIP\messi1.jpg')
image2=cv2.imread(r'2nd sem\DIP\messi2.jpg')
# Bitwise AND
result_and = cv2.bitwise_and(image1, image2)

# Bitwise OR
result_or = cv2.bitwise_or(image1, image2)

# Bitwise XOR
result_xor = cv2.bitwise_xor(image1, image2)

# Bitwise NOT (inverts image1)
result_not = cv2.bitwise_not(image1)

cv2.imshow('Bitwise AND', result_and)
cv2.imshow('Bitwise OR', result_or)
cv2.imshow('Bitwise XOR', result_xor)
cv2.imshow('Bitwise NOT', result_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
