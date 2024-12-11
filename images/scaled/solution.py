# Scale an image to be twice as big

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with twice the
# width and height of the original
(width, height) = im.size
output = Image.new(im.mode, (width * 2, height * 2))

for y in range(im.height * 2):
  for x in range(im.width * 2):
    (r, g, b) = im.getpixel((x // 2, y // 2))
    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("scaled.png")
