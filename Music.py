from pygame import mixer

class Music():
    def __init__(self, title, isInfinityPlaying):
        self.title = title
        self.isInfinityPlaying = isInfinityPlaying
        mixer.init()
        self.sound = mixer.Sound('music/' + self.title)

        #�eby muzyka gra�a w niesko�czono�� daje si� -1
        #�eby muzyka raz si� odtworzy�a daje si� 0
    def PlayMusic(self):
        #mixer.init()
        mixer.music.load('music/' + self.title)
        mixer.music.play(self.isInfinityPlaying)

    def PlayShoot(self):
        #mixer.init()
        #mixer.music.load('music/' + self.title)
        #mixer.music.play(self.isInfinityPlaying)
        
        mixer.Sound.play(self.sound)

