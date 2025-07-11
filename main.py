import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shots_fired = pygame.sprite.Group()
    Shot.containers = (shots_fired, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    initial_asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            dt = clock.tick(60) / 1000

        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game over!")
                pygame.quit()

        for asteroid in asteroids:
            for shot in shots_fired:
                if asteroid.collides(shot):
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
