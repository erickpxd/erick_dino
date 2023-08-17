import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hat import Hat
from dino_runner.utils.constants import SOUND_POWER_UP

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.choise = random.randint(0,1)

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(300, 400)
            if self.choise == 0:
                self.power_ups.append(Shield())
            elif self.choise == 1:
                self.power_ups.append(Hat())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if self.choise == 0:
                    game.player.shield = True
                    game.player.hat = False
                if self.choise == 1:
                    game.player.hat = True
                    game.player.shield = False
                SOUND_POWER_UP.play()
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 800)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.choise = random.randint(0,1)