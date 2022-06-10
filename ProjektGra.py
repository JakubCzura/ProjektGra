import pygame, os
import Resources
import Music
import Player, MainLevel, Alien
import random


pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
Screen = pygame.display.set_mode(Resources.ScreenSize)
Clock = pygame.time.Clock()


#konkretyzacja obiektow
Player = Player.Player(Resources.KAPITAN_R)
Player.rect.left = 150
Player.rect.bottom = 1000
MainLevel = MainLevel.MainLevel(Player)
Player.level = MainLevel

fps = 30 #liczba klatek na sekunde

MusicKarabinki = Music.Music('strzały_z_karabinow.wav', -1)
MusicKarabinki.PlayMusic()


ListOfAliens = pygame.sprite.Group()
ListOfPlayers = pygame.sprite.Group()


def AddAlienToList():
    leftOrRight = random.randint(0,1)
    if leftOrRight == 0:
        ListOfAliens.add(Alien.Alien(Resources.ALIEN_LEFT, Player, random.randint(0,100), random.randint(100,1100), MainLevel))
    else:
        ListOfAliens.add(Alien.Alien(Resources.ALIEN_LEFT, Player, random.randint(1800,1900), random.randint(100,1100), MainLevel))


def AddPlayerToList():
    ListOfPlayers.add(Player)

def UpdateAliens():
    for Alien in ListOfAliens:
        Alien.Update()

def DrawAliens():
    for Alien in ListOfAliens:
        Alien.Draw(Screen)


AddAlienToList()
AddPlayerToList()



def PlayGame():   
    GameLoop = True #petla gry
    TimeToSpawnAlien = 0 #poniewaz gra odswieza sie 30 klatek na sekunde to jesli wartosc osiagne 60 to znaczy ze kosmita pojawiac sie bedzie okolo 2 sekundy
    AmountOfAliens = 0
    
    while GameLoop:
        Screen.fill(Resources.LIGHTBLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameLoop = False
            Player.get_event(event)
     
        TimeToSpawnAlien += 1
        if TimeToSpawnAlien == 30:
            AddAlienToList()
            AmountOfAliens += 1
            TimeToSpawnAlien = 0

        pygame.sprite.groupcollide(MainLevel.DzidaBullets, ListOfAliens, True, True)
        pygame.sprite.groupcollide(MainLevel.KarabinekBullets, ListOfAliens, True, True)
        if pygame.sprite.groupcollide(ListOfPlayers, ListOfAliens, True, True) != {}: #jesli zderzy się gracz i kosmita to gra się konczy
            GameLoop = False
  
        UpdateAliens()
        Player.Update()    
        MainLevel.Update()
    
        Player.Draw(Screen)
        DrawAliens()
        MainLevel.Draw(Screen)
      
        #aktualizacja okna gry
        pygame.display.flip()
        Clock.tick(fps)


PlayGame()

pygame.quit()

print("Gra skończona")

