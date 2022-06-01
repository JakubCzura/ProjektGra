import pygame, os
import GameModule as GM
import Player, Item, Level, Level1, Platform

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
screen = pygame.display.set_mode(GM.SIZESCREEN)
clock = pygame.time.Clock()


#konkretyzacja obiektów
player = Player(GM.KAPITAN_R)
player.rect.left = 150
player.rect.bottom = GM.HEIGHT - 70
current_level = Level1(player)
player.level = current_level


window_open = True
#pêtla gry
while window_open:
    screen.fill(GM.LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        player.get_event(event)

    # aktualziacja i rysowanie obiektów
    player.update()
    current_level.update()

    player.draw(screen)
    current_level.draw(screen)


    #aktualizacja okna gry
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
