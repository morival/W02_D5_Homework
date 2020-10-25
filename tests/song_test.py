import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_01 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        self.song_02 = Song("Smoke on the Water", "Deep Purple", "Rock")
        self.song_03 = Song("Another Brick in the Wall", "Pink Floyd", "Rock")
        self.song_04 = Song("Satisfaction", "The Rolling Stones", "Rock")
        self.song_05 = Song("Kashmir", "Led Zeppelin", "Rock")
        self.song_06 = Song("Born to be Wild", "Steppenwolf", "Rock")
        self.song_07 = Song("We Will Rock You", "Queen", "Rock")
        self.song_08 = Song("Natural Mystic", "Bob Marley", "Reggae")
        self.song_09 = Song("Champion", "Buju Banton", "Reggae")
        self.song_10 = Song("O Carolina", "Shaggy", "Reggae")
        self.song_11 = Song("Get Busy", "Sean Paul", "Reggae")
        self.song_12 = Song("Vietnam", "Jimmy Cliff", "Reggae")
        self.song_13 = Song("Satta Massagana", "The Abyssinians", "Reggae")
        self.song_14 = Song("Boom Shiva", "Soom-T", "Reggae")
        self.song_15 = Song("Billie Jean", "Michael Jackson", "\'80s")
        self.song_16 = Song("Africa", "TOTO", "\'80s")
        self.song_17 = Song("Into the Groove", "Madonna", "\'80s")
        self.song_18 = Song("Roxanne", "The Police", "\'80s")
        self.song_19 = Song("When Doves Cry", "Prince", "\'80s")
        self.song_20 = Song("Eye of the Tiger", "Survivor", "\'80s")
        self.song_21 = Song("La Bamba", "Los Labos", "\'80s")

    # Song Title
    def test_check_song_title(self):
        self.assertEqual("Africa", self.song_16.title)

    # Song Artist
    def test_check_song_artist(self):
        self.assertEqual("Bob Marley", self.song_08.artist)

    # Song Genre
    def test_check_song_genre(self):
        self.assertEqual("Rock", self.song_04.genre)