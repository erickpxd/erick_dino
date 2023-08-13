import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        if self.type < 3:
            self.rect.y = 325
        elif self.type < 6:
            self.rect.y = 300