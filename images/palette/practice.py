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

def distance(c1, c2):
	(r1, g1, b1) = c1
	(r2, g2, b2) = c2

	# See https://en.wikipedia.org/wiki/Color_difference

	return # Your code goes here!

for y in range(im.height):
	for x in range(im.width):
		imgColor = im.getpixel((x, y))

		# Look through the colors in palette, and find
		# the one that is closest to the current pixel color

		# Use this closest palette color in the output image

		bestColor = None
		minDist = None

		# Your code goes here!

		# Loop through each color in the color palette

		# For each palette color, calculate the distance between
		# the current pixel color and the palette color. If the distance
		# is smaller than the current smallest distance (minDist), update
		# minDist and bestColor accordingly.

		# Once we've found the palette color which matches out pixel color
		# most closely, we use this closest color in out output image

		output.putpixel((x, y), bestColor)

# Save output image
output.save("palette.png")
