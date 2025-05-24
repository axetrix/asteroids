import sys

import pygame

# from constants import (
#     SCREEN_WIDTH, 
#     SCREEN_HEIGHT, 
#     ASTEROID_MIN_RADIUS, 
#     ASTEROID_KINDS, 
#     ASTEROID_SPAWN_RATE,
#     ASTEROID_MAX_RADIUS,
# )

from constants import *

from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroid_fields = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.has_collision(player):
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if asteroid.has_collision(shot):
                   shot.kill()
                   asteroid.split()

        screen.fill(color="#000000")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()