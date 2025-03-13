import math
import pygame

pygame.init()
# Screen is 800x800 pixels
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

class Planet():
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def draw(self):
        # Scale formula is kinda arbitrary, for aesthetics
        radius = 3 * self.mass ** 0.3
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), radius)

    def spawn(self, planets):
        # Generate a new planet object with update values based on list
        # of current objects and gravity equations

        ax = 0
        ay = 0

        for planet in planets:
            # Make sure we aren't calculating the gravity between a planet and itself
            if True:    # Change
                dx = 0  # Change
                dy = 0  # Change
                r = 0   # Change
                ax += 0 # Change
                ay += 0 # Change

        vx = self.vx # Change
        vy = self.vy # Change
        
        x = self.x # Change
        y = self.y # Change

        return Planet(x, y, vx, vy, self.mass)

planets = [
    Planet(300, 300, 0.012, -0.0432, 1000), # Why did I choose these velocities?
    Planet(300, 400, -2.4, 0, 5),
    Planet(550, 300, 0, 2, 20),
    Planet(565, 300, 0, 3.2, 1),
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
