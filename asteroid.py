import pygame
import random
from constants import *
from circleshape import *
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * (dt / 16)

    def split(self):
        self.kill()# Split the asteroid into two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = velocity2 * 1.2
        # Add the new asteroids to the game 
        