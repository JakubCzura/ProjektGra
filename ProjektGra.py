import pygame, os
#from pygame.locals import *
#from pygame import mixer
import game_module as gm
import Music
import Player, Platform, Item, Level, MainLevel

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
Screen = pygame.display.set_mode(gm.SIZESCREEN)
Clock = pygame.time.Clock()


#konkretyzacja obiekt�w
player = Player.Player(gm.KAPITAN_R)
player.rect.left = 150
player.rect.bottom = gm.HEIGHT - 70
MainLevel = MainLevel.MainLevel(player)
player.level = MainLevel

MusicKarabinki = Music.Music('strzały_z_karabinow.wav', -1)
MusicKarabinki.PlayMusic()

GameLoop = True
#p�tla gry
while GameLoop:
    Screen.fill(gm.LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameLoop = False
        player.get_event(event)

    # aktualziacja i rysowanie obiekt�w
    player.Update()
    MainLevel.Update()

    player.Draw(Screen)
    MainLevel.Draw(Screen)

   
    #aktualizacja okna gry
    pygame.display.flip()
    Clock.tick(30)

pygame.quit()

