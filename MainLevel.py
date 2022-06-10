import GameModule as gm
import Level, Platform, Item


class MainLevel(Level.Level):
    def __init__(self, player):
        super().__init__(player)
        self._CreatePlatforms()
        self._CreateItems()


    def _CreatePlatforms(self):
        platforms_cor = [[70, 70, 150, 1010], #kafelek kapitana
                         [70, 70, 150, 520],
                         [70, 70, 520, 530],
                         [70, 70, 1050, 520],
                         [70, 70, 1000, 1020]
                         ]
        
        #platforms_cor = []
        for cor in platforms_cor:
            self.platforms.add(Platform.Platform(gm.BORDER_LIST, *cor))

    def _CreateItems(self):
        karabinek = Item.Item(gm.KARABINEK, 'karabinek', 170, 480)
        karabinek2 = Item.Item(gm.KARABINEK, 'karabinek', 550, 490)
        dzida_laserowa = Item.Item(gm.LASEROWA_DZIDA, 'dzida_laserowa', 1080, 480)
        dzida_laserowa2 = Item.Item(gm.LASEROWA_DZIDA, 'dzida_laserowa', 1030, 980)
        self.ListOfWeapons.add(karabinek, karabinek2, dzida_laserowa, dzida_laserowa2)
        