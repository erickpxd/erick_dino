from dino_runner.utils.constants import HAT, HAT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hat(PowerUp):
    def __init__(self):
        self.image = HAT
        self.type = HAT_TYPE
        super().__init__(self.image, self.type)