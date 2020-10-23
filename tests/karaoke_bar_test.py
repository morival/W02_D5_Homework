import unittest
from classes.karaoke_bar import KaraokeBar
from classes.guest import *
from classes.room import *
from classes.song import *

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        
        self.guest = Guest()
        self.room = Room()
        self.song = Song()
        self.karaoke_bar = KaraokeBar(self.guest, self.room, self.song, "Screeching Seagull")

    def test_bar_name(self):
        self.assertEqual("Screeching Seagull", self.karaoke_bar.name)
    