# Invert the colors for each pixel in an image

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

# https://rgbcolorpicker.com/
# https://lospec.com/palette-list/

palette = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
]

# Calculate color distance between two colors
# https://en.wikipedia.org/wiki/Color_difference

def distance(c1, c2):
	(r1, g1, b1) = c1
	(r2, g2, b2) = c2
	return # Your code goes here!

for y in range(im.height):
	for x in range(im.width):
		imgColor = im.getpixel((x, y))

		# Your code goes here!

		output.putpixel((x, y), minColor)

# Save output image
output.save("palette.png")
