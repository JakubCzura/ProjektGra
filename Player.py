import pygame, os
import game_module as gm
import Bullet
import Music

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.rotate_left = False
        self.rotate_down = False
        self._count = 0
        self.level = None
        self.eq = {}
        self.speed = 4 #prędkość gracza

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_up(self):
        self.movement_y = -self.speed
        self.rotate_down = False

    def turn_down(self):
        self.movement_y = self.speed
        self.rotate_down = True

    def turn_right(self):
        self.movement_x = self.speed
        self.rotate_left = False

    def turn_left(self):
        self.movement_x = -self.speed
        self.rotate_left = True

    def stop_x(self):
        self.movement_x = 0

    def stop_y(self):
        self.movement_y = 0

    def shoot(self):
        #bronie muszą być poukładane od najlepszej żeby przerywać funkcję, gracz używa najkorzystniejszej broni
        #if self.eq.get('shotgun', 0) and len(self.level.set_of_bullets) < 3 :
        if self.eq.get('dzida_laserowa', 0):
            MusicDzida = Music.Music('strzał_z_dzidy.wav', 0)
            MusicDzida.PlayShoot()
            self.level.set_of_bullets.add(
                Bullet.Bullet(gm.DZIDA_POCISK, self.rotate_left, self.rect.centerx, self.rect.centery-10, 'dzida_laserowa'))
            return True
        if self.eq.get('karabinek', 0):
            MusicDzida = Music.Music('strzał_z_karabinu.wav', 0)
            MusicDzida.PlayShoot()
            self.level.set_of_bullets.add(
                Bullet.Bullet(gm.BULLET_LIST, self.rotate_left, self.rect.centerx , self.rect.centery -10, 'karabinek'))
            return True
        

    def update(self):

        # ruch w poziomie
        self.rect.x += self.movement_x

        # aniamcja
        if self.movement_x > 0:
            self._move(gm.PLAYER_RIGHT)
        if self.movement_x < 0:
            self._move(gm.PLAYER_LEFT)
        

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right


        # ruch w pionie
        self.rect.y += self.movement_y

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.movement_x == 0:
                    if self.rotate_left:
                        self.image = gm.KAPITAN_L
                    else:
                        self.image = gm.KAPITAN_R

            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0


        # kolizja z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.list_of_weapons, False)

        for item in colliding_items:
            if item.name == 'karabinek':
                self.eq[item.name] = 1
                item.kill()
            if item.name == 'dzida_laserowa':
                self.eq[item.name] = 1
                item.kill()
        print(self.eq)

    def get_event(self, event):
     
        #K_UP                 
        #K_DOWN                
        #K_RIGHT               
        #K_LEFT   
        
        #keydown jeśli klawisz jest wciśnięty
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.turn_right()
            if event.key == pygame.K_LEFT:
                self.turn_left()
            if event.key == pygame.K_UP:
                self.turn_up()
            if event.key == pygame.K_DOWN:
                self.turn_down()
            if event.key == pygame.K_SPACE:
                self.shoot()

        #keyup jeśli klawisz się zwalnia
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.turn_right()
            if event.key == pygame.K_LEFT:
                self.turn_left()
            if event.key == pygame.K_UP:
                self.turn_up()
            if event.key == pygame.K_DOWN:
                self.turn_down()
            

    def _move(self, image):
        self.image = image

