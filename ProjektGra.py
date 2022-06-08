import pygame, os
#from pygame.locals import *
#from pygame import mixer
import game_module as gm
import Music
import Player, Platform, Item, Level, Level_1

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()


#konkretyzacja obiekt�w
player = Player.Player(gm.KAPITAN_R)
player.rect.left = 150
player.rect.bottom = gm.HEIGHT - 70
current_level = Level_1.Level_1(player)
player.level = current_level

MusicKarabinki = Music.Music('strzały_z_karabinow.wav', -1)
MusicKarabinki.PlayMusic()

window_open = True
#p�tla gry
while window_open:
    screen.fill(gm.LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        player.get_event(event)

    # aktualziacja i rysowanie obiekt�w
    player.Update()
    current_level.Update()

    player.Draw(screen)
    current_level.draw(screen)

   
    #aktualizacja okna gry
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

