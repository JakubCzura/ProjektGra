
# okno główne
import pygame, os
SIZESCREEN = WIDTH, HEIGHT = 1366, 740


# kolory
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(SIZESCREEN)

# grafika  - wczytywanie grafik
#path = os.path.join(os.pardir, 'images')
#print(os.pardir)
path = 'images'

file_names = sorted(os.listdir(path))

#file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()


for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)


PLAYER_WALK_LIST_R = [KAPITAN_R, KAPITAN_R, KAPITAN_R,
                      KAPITAN_R, KAPITAN_R, KAPITAN_R,
                      KAPITAN_R, KAPITAN_R]


PLAYER_WALK_LIST_L = [KAPITAN_L, KAPITAN_L, KAPITAN_L,
                      KAPITAN_L, KAPITAN_L, KAPITAN_L,
                      KAPITAN_L, KAPITAN_L]

BORDER_LIST = [BORDER,BORDER,BORDER,BORDER]
