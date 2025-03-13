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

class Planet():
    def __init__(self, x, y, vx, vy, mass):
        # Store data in planet object
        pass

    def draw(self):
        # Scale formula is kinda arbitrary, for aesthetics
        radius = 3 * self.mass ** 0.3
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), radius)

    def spawn(self, others):
        # Generate a new planet object with update values based on list
        # of current objects and gravity equations

        ax = 0
        ay = 0

        for other in others:
            if True:    # Change
                dx = 0  # Change
                dy = 0  # Change
                r = 0   # Change
                ax += 0 # Change
                ay += 0 # Change

        vx = 0 # Change
        vy = 0 # Change
        
        x = 0 # Change
        y = 0 # Change

        return Planet(x, y, vx, vy, self.mass)

planets = [
    Planet(400, 400, 0.01125, -0.0267, 2000),
    Planet(400, 500, -4.5, 0, 5),
    Planet(700, 100, 0, 2, 1),
    Planet(750, 390, 0, 2.4, 20),
    Planet(770, 390, 0, 3.4, 1),
]

running = True

while running:
    # Pygame makes us reinvent the wheel (game loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background to clear screen
    screen.fill("#00132e")

    for planet in planets:
      planet.draw()

    planets = [p.spawn(planets) for p in planets]

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
