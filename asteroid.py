import random

import pygame

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def __move(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

        return super().draw(screen)

    def update(self, dt):
        self.__move(dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2
        
        radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position

        asteroid1 = Asteroid(x, y, radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(x, y, radius)
        asteroid2.velocity = velocity2
        

        