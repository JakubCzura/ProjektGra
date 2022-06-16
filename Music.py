from pygame import mixer

class Music():
    def __init__(self, title, isInfinityPlaying):
        self.title = title
        self.isInfinityPlaying = isInfinityPlaying
        mixer.init()
        self.sound = mixer.Sound('music/' + self.title)

        #zeby muzyka grala w nieskonczonosc daje sie isInfinityPlaying  -1
        #zeby muzyka grala raz daje sie isInfinityPlaying  0
    def PlayMusic(self):
        mixer.music.load('music/' + self.title)
        mixer.music.play(self.isInfinityPlaying)

    def PlayShoot(self):       
        mixer.Sound.play(self.sound)


