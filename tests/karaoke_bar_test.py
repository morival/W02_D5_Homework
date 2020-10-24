import unittest

from classes.guest import *
from classes.room import *
from classes.song import *
from classes.karaoke_bar import *

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        
        self.guest = Guest("John Stone", "checked-in", 50.00, "Kashmir", "\'80")
        self.room = Room()
        self.song = Song("Kashmir", "Led Zeppelin", "Rock")
        self.karaoke_bar = KaraokeBar(self.guest, self.room, self.song, "Screeching Seagull")

    def test_bar_has_name(self):
        self.assertEqual("Screeching Seagull", self.karaoke_bar.bar_name)
    
    