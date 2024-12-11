print("CS 2 Info")

print({
  "name": "Avery Nortonsmith",
  "email": "anortonsmith@germantownfriends.org",
})

description = """
As a second-year programming course, this class will explore the real-world applications of software
development. How does Google know what pages to recommend in a search result? How do Instagram filters
change the way photos look? How does a calendar application calculate when repeating events will next
occur? Students will find answers to these questions and more in this project-based class.
"""

print(description.replace("\n", " ").strip())

topics = [
  "Data analysis",
  "Text processing",
  "Web scraping",
  "Image processing",
  "Automation",
  "Algorithms",
  "Data structures",
  "Simulation",
  "Mathematical programming",
]

print("\n".join(f"• {topic}" for topic in topics))

# This demo preserves the colors for pixels that are "red-ish" (more red than blue or green), and sets
# the other pixels to grayscale. In the demo image below, we see that the reds and yellows in the bird
# are preserved, while the blues and greens of the background are removed.

from PIL import Image

im = Image.open("bird.png")
output = Image.new(im.mode, im.size)

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    if r < g or r < b:
      l = round((r + g + b) / 3)
      output.putpixel((x, y), (l, l, l))
    else:
      output.putpixel((x, y), (r, g, b))

output.save("output.png")
