import pygame

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.gun_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def __shot(self):
        if self.gun_timer > 0:
            return

        self.gun_timer = PLAYER_SHOOT_COOLDOWN

        Shot(self.position.x, self.position.y, self.rotation)
    
    def __rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def __move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        self.position += forward * PLAYER_SPEED * dt
    
    def draw(self, screen):
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=2)

        return super().draw(screen)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.gun_timer -= dt

        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
             self.__rotate(dt)
        if keys[pygame.K_w]:
            self.__move(dt)
        if keys[pygame.K_s]:
             self.__move(-dt)

        if keys[pygame.K_SPACE]:
            self.__shot()