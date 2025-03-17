import math
import pygame

sunX = 300
sunY = 300
sunMass = 1000

pygame.init()
# Screen is 600x600 pixels
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class Planet():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self):
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), 5)

    def calcAcceleration(self):
        # Calculate acceleration from gravity equation
        dx = sunX - self.x
        dy = sunY - self.y
        r = math.sqrt(dx ** 2 + dy ** 2)
        self.ax = dx * sunMass / r ** 3
        self.ay = dy * sunMass / r ** 3

    def move(self):
        # Update position and velocty based on acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

planet = Planet(100, 300, 0, -1.5)

running = True

while running:
    # Pygame makes us reinvent the wheel (game loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background to clear screen
    screen.fill("#00132e")

    # Draw sun
    pygame.draw.circle(screen, "#ff9c7a", (sunX, sunY), 20)

    planet.draw()
    planet.calcAcceleration()
    planet.move()

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
