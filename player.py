from circleshape import *
from constants import *
from shot import Shot

shots_group = pygame.sprite.Group() 

class Player(CircleShape) :
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0 
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]        
            
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

        
    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def move(self,dt) :
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

     

    def shoot(self):
    # Check if the timer has expired to allow shooting
        if self.timer <= 0:
            # Create a new shot and add it to the group
            new_shot = Shot(self.position, self.rotation)
            shots_group.add(new_shot)
            
            # Reset the shooting timer
            self.timer = PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt
        if keys[pygame.K_a]:            
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt) 
        if keys[pygame.K_s]:
            self.move(-dt) 
        if keys[pygame.K_w]:
            self.move(dt) 
        if keys[pygame.K_SPACE]:
            self.shoot()    
