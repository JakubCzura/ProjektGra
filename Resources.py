import pygame, os

ScreenSize = width, height = 1920, 1080

# kolory
deepSkyBlue1 = pygame.color.THECOLORS['deepskyblue1']
lightBlue = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(ScreenSize) #okno gry

imageDirectoryPath = 'images' #folder z grafik¹

imageList = sorted(os.listdir(imageDirectoryPath)) #lista zdjêæ z folderu

for file_name in imageList:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(imageDirectoryPath, file_name)).convert_alpha() #obciêcie z nazwy zdjêcia ".png" i przekonwertowanie na odpowiedni format convert_alpha()


PLAY_BUTTON = PLAY_BUTTON
ESCAPE_BUTTON = ESCAPE_BUTTON

KAPITAN_RIGHT = KAPITAN_R
KAPITAN_LEFT = KAPITAN_L

ALIEN_RIGHT = ALIEN_R
ALIEN_LEFT = ALIEN_L

GROUND = GROUND

BULLET_LIST = [BULLET_R, BULLET_L]
DZIDA_POCISK = [DZIDA_POCISK, DZIDA_POCISK]