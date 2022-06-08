# okno główne
import pygame, os

SIZESCREEN = WIDTH, HEIGHT = 1920, 1080


# kolory
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(SIZESCREEN)


path = 'images'

file_names = sorted(os.listdir(path))

#file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()


for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)


KAPITAN_RIGHT = KAPITAN_R

KAPITAN_LEFT= KAPITAN_L

BORDER_LIST = [BORDER,BORDER,BORDER,BORDER]

BULLET_LIST = [BULLET_R, BULLET_L]

DZIDA_POCISK = [DZIDA_POCISK, DZIDA_POCISK]
