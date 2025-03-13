import math
import pygame

pygame.init()
# Screen is 600x600 pixels
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

ax = 0
ay = 1

class Projectile():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self):
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), 10)

    def move(self):
        # Update projectile data based on motion equations
        pass

proj = Projectile(50, 550, 5, -25)

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
