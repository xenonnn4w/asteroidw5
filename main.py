import pygame
from constants import *
from player import Player
import asteroidfield
from asteroid import Asteroid
import sys
from shot import Shot

def main():
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    dt = 0 
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield.AsteroidField()
    

    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for sprite in updatable:
         sprite.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("game over")
                sys.exit()
      
        for asteroid in asteroids :
           for shot in shots :
              if shot.collision(asteroid):
                 shot.kill()
                 asteroid.split()

        for sprite in drawable:
         sprite.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000 

    


if __name__ == "__main__":
    main()
