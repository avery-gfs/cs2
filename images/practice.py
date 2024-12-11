# TO DO: reformat problems into code, write different image for each problem, add demo images

# **Invert:** Write a program to invert the colors for each pixel in an image.

# **Grayscale:** Write a program to convert an image to grayscale.

# **Black and White:** Write a program to convert an image to black-and-white.

# **Color Channels:** Write a program to convert any green-ish pixels (pixels that are more green than they are red or blue) to grayscale.

# **Transformation:** Write a program to rotate an image `n` degrees about its center.


from PIL import Image

im = Image.open("bird.png") # load input image
output = Image.new(im.mode, im.size) # make blank output image with same dimension as input

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    # your code here

    output.putpixel((x, y), (r, g, b))

output.save("output.png") # save output image
