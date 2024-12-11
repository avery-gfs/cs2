# Convert the green-ish pixels (pixels that are more green
# than they are red or blue) in an image to grayscale

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    if g > r and g > b:
      l = round(0.2126 * r + 0.7152 * g + 0.0722 * b)
      r = l
      g = l
      b = l

    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("greenish.png")
