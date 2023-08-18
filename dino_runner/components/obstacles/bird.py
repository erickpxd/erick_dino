import random
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        self.step_index = 0
        bird_locate = random.randint(0,2)
        super().__init__(image, self.type)
        if bird_locate ==0:
            self.rect.y = 475
        elif bird_locate ==1:
            self.rect.y = 435
        else:
            self.rect.y = 375
    
    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1
        if self.step_index >= 9:
            self.step_index = 0