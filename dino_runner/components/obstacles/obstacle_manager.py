import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LIXOS, BIRD,SOUND_CLS, SOUND_DIE
import random
pygame.init()

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.choise = random.randint(0,2)
        if len(self.obstacles) == 0:
            if self.choise > 0:
                self.obstacles.append(Cactus(LIXOS))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    SOUND_DIE.play()
                    break
                elif isinstance(obstacle, Cactus) and game.player.type == 'shield':
                    self.obstacles.remove(obstacle)
                    SOUND_CLS.play()
                elif isinstance(obstacle, Bird) and game.player.type == 'hat':
                    self.obstacles.remove(obstacle)
                    SOUND_CLS.play()
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    SOUND_DIE.play()
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []