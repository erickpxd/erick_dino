import pygame
import os
pygame.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "imagens/DIE.png"))
ICON = pygame.transform.scale(ICON, (140, 130))
# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "imagens/START.png"))
DINO_START = pygame.transform.scale(DINO_START, (140, 130))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "imagens/DIE.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN2.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN1E.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN2E.png")),
]
RUNNING_HAT = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN1C.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/RUN2C.png"))
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK2.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK1E.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK2E.png")),
]
DUCKING_HAT = [
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK1C.png")),
    pygame.image.load(os.path.join(IMG_DIR, "imagens/DUCK2C.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "imagens/JUMP.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "imagens/JUMPECO.png")
)
JUMPING_HAT = pygame.image.load(os.path.join(IMG_DIR, "imagens/JUMPBIT.png")
)

# Obstacles
LIXOS = []
# Carrega as imagens de lixo
lixos1 = pygame.image.load(os.path.join(IMG_DIR, "imagens/LIXO1.png"))
lixos2 = pygame.image.load(os.path.join(IMG_DIR, "imagens/LIXO2.png"))
lixos3 = pygame.image.load(os.path.join(IMG_DIR, "imagens/LIXO3.png"))
lixos4 = pygame.image.load(os.path.join(IMG_DIR, "imagens/Lixo4.png"))
lixos5 = pygame.image.load(os.path.join(IMG_DIR, "imagens/Lixo5.png"))

# Redimensiona as imagens para 120 por 120 pixels
lixos1 = pygame.transform.scale(lixos1, (120, 110))
lixos2 = pygame.transform.scale(lixos2, (120, 110))
lixos3 = pygame.transform.scale(lixos3, (120, 110))
lixos4 = pygame.transform.scale(lixos4, (120, 110))
lixos5 = pygame.transform.scale(lixos5, (120, 110))

# Adiciona as imagens à lista `LIXOS`
LIXOS.append(lixos1)
LIXOS.append(lixos2)
LIXOS.append(lixos3)
LIXOS.append(lixos4)
LIXOS.append(lixos5)

#BIRD
bird1 = pygame.image.load(os.path.join(IMG_DIR, "imagens/Bird1.png"))
bird2 = pygame.image.load(os.path.join(IMG_DIR, "imagens/Bird2.png"))

bird1 = pygame.transform.scale(bird1, (80, 80))
bird2 = pygame.transform.scale(bird2, (80, 80))

BIRD = []
BIRD.append(bird1)
BIRD.append(bird2)



# Power ups
escudo = pygame.image.load(os.path.join(IMG_DIR, "imagens/eco.png"))
SHIELD = pygame.transform.scale(escudo, (120, 120))
hat = pygame.image.load(os.path.join(IMG_DIR, "imagens/BIT.png"))
HAT = pygame.transform.scale(hat, (120, 120))

BG = pygame.image.load(os.path.join(IMG_DIR, "imagens/Track.png"))
BIG_BG = pygame.image.load(os.path.join(IMG_DIR, "imagens/bg1.png"))
BIG_BG = pygame.transform.scale(BIG_BG, (SCREEN_WIDTH,SCREEN_HEIGHT))
PARALAX1 = pygame.image.load(os.path.join(IMG_DIR, "imagens/Paralax_1.png"))
PARALAX1 = pygame.transform.scale(PARALAX1, (SCREEN_WIDTH,SCREEN_HEIGHT))
PARALAX2 = pygame.image.load(os.path.join(IMG_DIR, "imagens/paralax_final.png"))
PARALAX2 = pygame.transform.scale(PARALAX2, (SCREEN_WIDTH,SCREEN_HEIGHT))



MP3 = pygame.mixer.music.load(os.path.join(IMG_DIR,"Other/praieira.mp3"))
SOUND_CLS = pygame.mixer.Sound(os.path.join(IMG_DIR,"Other/CLS.wav"))
SOUND_JUMP = pygame.mixer.Sound(os.path.join(IMG_DIR,"Other/JUMP.wav"))
SOUND_DIE = pygame.mixer.Sound(os.path.join(IMG_DIR,"Other/DIE.wav"))
SOUND_POWER_UP = pygame.mixer.Sound(os.path.join(IMG_DIR,"Other/POWER_UP.wav"))
SOUND_START = pygame.mixer.Sound(os.path.join(IMG_DIR,"Other/START.wav"))

pygame.mixer.music.set_volume(0.2)
SOUND_CLS.set_volume(0.3)
SOUND_JUMP.set_volume(0.3)
SOUND_DIE.set_volume(0.3)
SOUND_POWER_UP.set_volume(0.3)
SOUND_START.set_volume(0.3)

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAT_TYPE = "hat"
