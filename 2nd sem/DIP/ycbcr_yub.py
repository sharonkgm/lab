import cv2
import numpy as np

image_rgb = cv2.imread(r'2nd sem\DIP\messi1.jpg')

# Convert the RGB image to YCbCr color space
image_ycbcr = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2YCrCb)

# Convert the RGB image to YUV color space
image_yuv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2YUV)

# Split the channels of the YCbCr image
y, cr, cb = cv2.split(image_ycbcr)

# Split the channels of the YUV image
y, u, v = cv2.split(image_yuv)

# Display the channels
cv2.imshow('Y (Luma) - YCbCr', y)
cv2.imshow('Cb (Blue Chroma) - YCbCr', cb)
cv2.imshow('Cr (Red Chroma) - YCbCr', cr)

cv2.imshow('Y (Luma) - YUV', y)
cv2.imshow('U (Chrominance) - YUV', u)
cv2.imshow('V (Chrominance) - YUV', v)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
