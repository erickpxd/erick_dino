import pygame
from dino_runner.utils.constants import (
    RUNNING,
    JUMPING,
    DUCKING,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    DUCKING_SHIELD,
    RUNNING_HAT,
    JUMPING_HAT,
    DUCKING_HAT,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    HAT_TYPE,
    SOUND_JUMP

)
from pygame.sprite import Sprite
pygame.init()


X_POS = 80
Y_POS = 485
JUMP_VEL = 8.5


DUCK_IMG = {
    DEFAULT_TYPE: DUCKING,
    SHIELD_TYPE: DUCKING_SHIELD,
    HAT_TYPE: DUCKING_HAT 
}
JUMP_IMG = {
    DEFAULT_TYPE: JUMPING,
    SHIELD_TYPE: JUMPING_SHIELD,
    HAT_TYPE: JUMPING_HAT
}
RUN_IMG = {
    DEFAULT_TYPE: RUNNING,
    SHIELD_TYPE: RUNNING_SHIELD,
    HAT_TYPE: RUNNING_HAT
}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_test = False
        self.hat = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            SOUND_JUMP.play()
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.image = pygame.transform.scale(self.image,(84,84))
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.dino_rect.x = X_POS
        self.image = JUMP_IMG[self.type]
        self.image = pygame.transform.scale(self.image,(84,84))
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
        

    def duck(self):
        if not self.type == 'hat':
            self.image = DUCK_IMG[self.type][self.step_index // 5]
            self.image = pygame.transform.scale(self.image,(60,40))
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS +13
            self.dino_rect.y = Y_POS + 44
            self.step_index += 1
            self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))