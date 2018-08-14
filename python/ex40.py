class Song(object):
    def__init_(self, lyrics):
        self.lyrics = lyrics
    def__sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = song(["happy birthday to you"
                  "i dont want to get sued"
                  "so i will stop right there" ])

bulls_on_parade = song(["They rally around the family"
                         "with pockets full of shells"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
