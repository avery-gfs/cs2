import math
import pygame

pygame.init()
# Screen is 600x600 pixels
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class Planet():
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0
        self.mass = mass

    def draw(self):
        # Scale formula is kinda arbitrary, for aesthetics
        radius = 2 * self.mass ** 0.3
        pygame.draw.circle(screen, "#ff9c7a", (self.x, self.y), radius)

    def calcAcceleration(self, planets):
        # Calculate acceleration from gravity equation
        self.ax = 0
        self.ay = 0

        for planet in planets:
            # Make sure we aren't calculating the gravity between a planet and itself
            if planet != self:
                dx = planet.x - self.x
                dy = planet.y - self.y
                r = math.sqrt(dx ** 2 + dy ** 2)
                self.ax += dx * planet.mass / r ** 3
                self.ay += dy * planet.mass / r ** 3

    def move(self):
        # Update position and velocty based on acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

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
      planet.calcAcceleration(planets)

    for planet in planets:
      planet.move()

    # Limit to 50 fps
    clock.tick(50)
    # Redraw game canvas
    pygame.display.flip()
