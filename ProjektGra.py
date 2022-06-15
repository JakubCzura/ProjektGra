import pygame, os
import Resources
import Music
import Player, MainLevel, Alien, Menu
import random

pygame.init()

gameMode = 'normal'

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


def PlayGame(gameMode='normal'):
    ListOfAliens = pygame.sprite.Group()
    ListOfPlayers = pygame.sprite.Group()

    def AddAlienToList(alienSpeed):
        leftOrRight = random.randint(0,1)
        if leftOrRight == 0:
            ListOfAliens.add(Alien.Alien(Resources.ALIEN_LEFT, Player, random.randint(0,100), random.randint(100,1100), MainLevel, alienSpeed))
        else:
            ListOfAliens.add(Alien.Alien(Resources.ALIEN_LEFT, Player, random.randint(1800,1900), random.randint(100,1100), MainLevel, alienSpeed))

    def AddPlayerToList():
        ListOfPlayers.add(Player)

    def UpdateAliens():
        for Alien in ListOfAliens:
            Alien.Update()

    def DrawAliens():
        for Alien in ListOfAliens:
            Alien.Draw(Screen)

    AddPlayerToList()  

    SpawnAlien = 10
    if gameMode == 'normal':
        SpawnAlien = 30
    elif gameMode == 'hard':
        SpawnAlien = 5
    GameLoop = True #petla gry
    TimeToSpawnAlien = 0 
    
    while GameLoop:
        Screen.fill(Resources.deepSkyBlue1)
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
            #    GameLoop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameLoop = False
            Player.get_event(event)

        TimeToSpawnAlien += 1

        if gameMode == 'normal':      
            if TimeToSpawnAlien == SpawnAlien: #poniewaz gra odswieza sie 30 klatek na sekunde to jesli wartosc osiagne 60 to znaczy ze kosmita pojawiac sie bedzie okolo 2 sekundy
                AddAlienToList(2)
                TimeToSpawnAlien = 0
        elif gameMode == 'hard':
             if TimeToSpawnAlien == SpawnAlien: 
                AddAlienToList(6)
                TimeToSpawnAlien = 0

        pygame.sprite.groupcollide(MainLevel.DzidaBullets, ListOfAliens, True, True)
        pygame.sprite.groupcollide(MainLevel.KarabinekBullets, ListOfAliens, True, True)
        if pygame.sprite.groupcollide(ListOfPlayers, ListOfAliens, True, True) != {}: #jesli zderzy się gracz i kosmita to gra się konczy
            GameLoop = False
            #pygame.quit() #koniec gry
        
        UpdateAliens()
        Player.Update()    
        MainLevel.Update()
    
        Player.Draw(Screen)
        DrawAliens()
        MainLevel.Draw(Screen)
      
        #aktualizacja okna gry
        pygame.display.flip()
        Clock.tick(fps)


def ShowMenu():
    MenuLoop = True #petla menu
    WelcomeMessage = Menu.Menu(450, 50, 'WELCOME_BUTTON')
    PlayMessage = Menu.Menu(700, 300, 'PLAY_BUTTON')
    PlayHardMessage= Menu.Menu(700, 550, 'PLAY_HARD_BUTTON')
    EscapeMessage= Menu.Menu(700, 800, 'ESCAPE_BUTTON')
    
    while MenuLoop:
        Screen.fill(Resources.lightBlue)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #wcisnij esc zeby wyjsc6
                    MenuLoop = False
                if event.key == pygame.K_p: #wcisnij p zeby grac
                    gameMode = 'normal'
                    PlayGame(gameMode)
                if event.key == pygame.K_e: #wcisnij e zeby zagrac ekstremalnie
                    gameMode = 'hard'
                    PlayGame(gameMode)
      
        #aktualizacja okna gry
        WelcomeMessage.Draw(Screen)
        PlayHardMessage.Draw(Screen)
        PlayMessage.Draw(Screen)
        EscapeMessage.Draw(Screen)
        pygame.display.flip()
        Clock.tick(fps)

ShowMenu()

pygame.quit()

print("Dziękujemy za zagranie\nGra skończona")

