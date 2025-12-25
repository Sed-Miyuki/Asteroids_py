from circle_shape import *
from constants import *
from main import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        angle=random.uniform(20,50)
        a1=self.velocity.rotate(angle)
        a2=self.velocity.rotate(-angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        [x,y]=self.position
        astra1=Asteroid(x,y,new_radius)
        astra2=Asteroid(x,y,new_radius)
        astra1.velocity=a1*1.2
        astra2.velocity=a2*1.2
        
    