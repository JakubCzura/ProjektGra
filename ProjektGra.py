from turtle import update
import pygame, os
#from pygame.locals import *
#from pygame import mixer
import game_module as gm
import Music
import Player, Platform, Item, Level, MainLevel, Alien
import random


pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
Screen = pygame.display.set_mode(gm.SIZESCREEN)
Clock = pygame.time.Clock()


#konkretyzacja obiektow
player = Player.Player(gm.KAPITAN_R)
player.rect.left = 150
player.rect.bottom = gm.HEIGHT - 70
MainLevel = MainLevel.MainLevel(player)
player.level = MainLevel


MusicKarabinki = Music.Music('strzały_z_karabinow.wav', -1)
MusicKarabinki.PlayMusic()


ListOfAliens = pygame.sprite.Group()

def AddAlienToList():
    ListOfAliens.add(Alien.Alien(gm.ALIEN_LEFT, player, random.randint(100,1100), random.randint(100,1100), MainLevel))



def UpdateAliens():
    for Alien in ListOfAliens:
        Alien.Update()

def DrawAliens():
    for Alien in ListOfAliens:
        Alien.Draw(Screen)


AddAlienToList()
GameLoop = True

TimeToSpawnAlien = 0 #poniewaz gra odswieza sie 30 klatek na sekunde to jesli wartosc osiagne 40 to znaczy ze kosmita pojawiac sie bedzie okolo 1,3 sekundy

#petla gry
while GameLoop:
    Screen.fill(gm.LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameLoop = False
        player.get_event(event)

    # aktualziacja i rysowanie obiektow
    player.Update()
    
    TimeToSpawnAlien += 1
    if TimeToSpawnAlien == 40:
        AddAlienToList()
        TimeToSpawnAlien = 0

    pygame.sprite.groupcollide(MainLevel.DzidaBullets, ListOfAliens, True, True)
    pygame.sprite.groupcollide(MainLevel.KarabinekBullets, ListOfAliens, True, True)
    pygame.sprite.groupcollide(player, ListOfAliens, True, False)
    
    UpdateAliens()
    
    MainLevel.Update()
    


    player.Draw(Screen)

    DrawAliens()

    MainLevel.Draw(Screen)

   
    #aktualizacja okna gry
    pygame.display.flip()
    Clock.tick(30)

pygame.quit()

