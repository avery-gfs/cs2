# Convert an image to black and white

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    average = round((r + g + b) / 3)
    bw = 255 if average > 128 else 0

    r = bw
    g = bw
    b = bw

    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("black-and-white.png")
