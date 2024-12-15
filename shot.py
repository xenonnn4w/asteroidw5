from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, position, angle):
        # Call CircleShape's __init__ with the correct parameters
        # Remember CircleShape expects x, y, radius as separate parameters ahh
        super().__init__(position.x, position.y, SHOT_RADIUS)
        
        direction = pygame.Vector2(0,1).rotate(angle)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt