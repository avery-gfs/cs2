# Convert an image to grayscale using the relative luminance formula
# https://en.wikipedia.org/wiki/Relative_luminance

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    # Your code goes here !!

    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("fancy-grayscale.png")
