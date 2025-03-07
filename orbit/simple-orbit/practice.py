import math
import pygame

# Gravity
g = 1
# Simulation time delta
dt = 1

sunX = 400
sunY = 400
sunMass = 2000

pygame.init()
# Screen is 800x800 pixels
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

class Planet():
    def __init__(self, x, y, vx, vy):
        # Store data in planet object
        pass

    def draw(self):
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), 5)

    def move(self):
        # Update planet data based on sun variables and gravity equations
        pass

planet = Planet(100, 400, 0, -2)

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
    planet.move()

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
