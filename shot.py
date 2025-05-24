import pygame

from circleshape import CircleShape

from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)

        self.rotation = rotation

    def __move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        self.position += forward * PLAYER_SHOOT_SPEED * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

        return super().draw(screen)

    def update(self, dt):
        self.__move(dt)
        