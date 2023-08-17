import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 4)
        super().__init__(image, self.type) 
        if self.type == 0:
            self.rect.y = 476
        elif self.type == 2:
            self.rect.y = 510
        else:
            self.rect.y = 465