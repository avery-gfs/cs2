import math
import pygame

# Gravity
g = 1
# Simulation time delta
dt = 1

pygame.init()
# Screen is 800x800 pixels
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

class Projectile():
    def __init__(self, x, y, vx, vy):
        # Store data in projectile object
        pass

    def draw(self):
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), 10)

    def move(self):
        # Update projectile data based on motion equations
        pass

proj = Projectile(100, 700, 10, -30)

running = True

while running:
    # Pygame makes us reinvent the wheel (game loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background to clear screen
    screen.fill("#00132e")

    proj.draw()
    proj.move()

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
