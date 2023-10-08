#Read an RGB image and Display its Channels

# pip install pillow

from PIL import Image

image = Image.open(r'2nd sem\DIP\messi1.jpg')

image = image.convert('RGB')

# Split the image into its channels
r, g, b = image.split()

# Display each channel
r.show(title='Red channel')
g.show(title='Green channel')
b.show(title='Blue channel')
