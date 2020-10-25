import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("John Stone", "waiting", 50.00, "Kashmir", "Michael Jackson")
        self.guest_02 = Guest("Mia Wong", "waiting", 12.00, "Roxanne", "Prince")
        self.guest_03 = Guest("Natalie Lee-Walsh", "waiting", 406.50, "O Carolina", "The Rolling Stones")
        self.guest_04 = Guest("Ang Li", "waiting", 40.50, "Eye of the Tiger", "Sean Paul")
        self.guest_05 = Guest("Nguta Ithya", "waiting", 36.50, "Natural Mystic", "Pink Floyd")
        self.guest_06 = Guest("Tamzyn French", "waiting", 98.00, "We Will Rock You", "Michael Jackson")
        self.guest_07 = Guest("Salome Simoes", "waiting", 27.20, "Boom Shiva", "Madonna")
        self.guest_08 = Guest("Trevor Virtue", "waiting", 21.90, "La Bamba", "AC/DC")
        self.guest_09 = Guest("Eugenia Anders", "waiting", 320.00, "Africa", "Nirvana")
        self.guest_10 = Guest("Tarryn Campbell-Gillies", "waiting", 46.50, "When Doves Cry", "The Police")
        self.guest_11 = Guest("Andrew Kazantzis", "waiting", 82.50, "Smells Like Teen Spirit", "Michael Jackson")
        self.guest_12 = Guest("Verona Blair", "waiting", 6.50, "Into the Groove", "Bob Marley")
        self.guest_13 = Guest("Jane Meldrum", "waiting", 116.30, "Born to be Wild", "Shaggy")
        self.guest_14 = Guest("Maureen M. Smith", "waiting", 12.70, "Get Busy", "Soom-T")
        self.guest_15 = Guest("Desiree Burch", "waiting", 61.00, "Another Brick in the Wall", "Madonna")
        self.guest_16 = Guest("Daly Harry", "waiting", 47.80, "Billie Jean", "TOTO")
        self.guest_17 = Guest("Hayman Andrews", "waiting", 59.10, "Vietnam", "Sean Paul"), 
        self.guest_18 = Guest("Ruveni Ellawala", "waiting", 3.50, "Smoke on the Water", "Prince")
    
        
# Create New Guest
    # def test_create_new_guest(self):
    #     self.assertEqual()

# Guest Name
    def test_check_guest_name(self):
        self.assertEqual("John Stone", self.guest_01.name)

# Guest Status
    def test_check_guest_status(self):
        self.assertEqual("waiting", self.guest_01.status)

# Guest Wallet
    def test_check_guest_wallet(self):
        self.assertEqual(12.00, self.guest_02.wallet)
        
# Guest Favourite Song
    def test_check_guest_fav_song(self):
        self.assertEqual("Roxanne", self.guest_02.favourite_song)
    
# Guest disliked artist
    def test_check_guest_disliked_artist(self):
        self.assertEqual("Madonna", self.guest_15.disliked_artist)