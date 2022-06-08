import pygame, os
import game_module as gm
import Level, Platform, Item


class Level_1(Level.Level):
    def __init__(self, player):
        super().__init__(player)
        self._CreatePlatforms()
        self._CreateItems()


    def _CreatePlatforms(self):
        platforms_cor = [[1000*70, 70, 70, gm.HEIGHT - 70],
                         [1000*70, 70, 200, gm.HEIGHT-740],
                         [70, 70, 1000, 370],
                         ]
        
        #platforms_cor = []
        for cor in platforms_cor:
            self.set_of_platforms.add(Platform.Platform(gm.BORDER_LIST, *cor))

    def _CreateItems(self):
        karabinek = Item.Item(gm.KARABINEK, 'karabinek', 1000, 220)
        karabinek2 = Item.Item(gm.KARABINEK, 'karabinek', 750, 620)
        dzida_laserowa = Item.Item(gm.LASEROWA_DZIDA, 'dzida_laserowa', 50, 300)
        dzida_laserowa2 = Item.Item(gm.LASEROWA_DZIDA, 'dzida_laserowa', 350, 520)
        self.ListOfWeapons.add(karabinek, karabinek2, dzida_laserowa, dzida_laserowa2)
        