import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("John Stone", "checked-in", 50.00, "Kashmir", "Michael Jackson")
        self.guest_02 = Guest("Mia Wong", "waiting", 12.00, "Roxanne", "Prince")
        self.guest_03 = Guest("Natalie Lee-Walsh", "checked-out", 406.50, "O Carolina", "The Rolling Stones")
        self.guest_04 = Guest("Ang Li", "waiting", 40.50, "Eye of the Tiger", "Sean Paul")
        self.guest_05 = Guest("Nguta Ithya", "waiting", 36.50, "Natural Mystic", "Pink Floyd")
        self.guest_06 = Guest("Tamzyn French", "checked-in", 98.00, "We Will Rock You", "Michael Jackson")
        self.guest_07 = Guest("Salome Simoes", "checked-in", 27.20, "Boom Shiva", "Madonna")
        self.guest_08 = Guest("Trevor Virtue", "waiting", 21.90, "La Bamba", "AC/DC")
        self.guest_09 = Guest("Eugenia Anders", "checked-out", 320.00, "Africa", "Nirvana")
        self.guest_10 = Guest("Tarryn Campbell-Gillies", "checked-in", 46.50, "When Doves Cry", "The Police")
        self.guest_11 = Guest("Andrew Kazantzis", "checked-out", 82.50, "Smells Like Teen Spirit", "Michael Jackson")
        self.guest_12 = Guest("Verona Blair", "waiting", 6.50, "Into the Groove", "Bob Marley")
        self.guest_13 = Guest("Jane Meldrum", "waiting", 116.30, "Born to be Wild", "Shaggy")
        self.guest_14 = Guest("Maureen M. Smith", "checked-in", 12.70, "Get Busy", "Soom-T")
        self.guest_15 = Guest("Desiree Burch", "checked-in", 61.00, "Another Brick in the Wall", "Madonna")
        self.guest_16 = Guest("Daly Harry", "waiting", 47.80, "Billie Jean", "TOTO")


# Guest Name
    def test_check_guest_name(self):
        self.assertEqual("John Stone", self.guest_01.name)

# Guest Status
    def test_check_guest_status(self):
        self.assertEqual("checked-in", self.guest_01.status)

    def test_check_if_guest_can_checkin(self):
        self.guest_02.check_if_guest_can_checkin()
        self.assertEqual(True, self.guest_02.check_if_guest_can_checkin())

    def test_checkin_guest(self):
        self.guest_02.checking_in_guest()
        self.assertEqual("checked-in", self.guest_02.status)

    def test_check_if_guest_can_checkout(self):
        self.guest_01.check_if_guest_can_checkout()
        self.assertEqual(True, self.guest_01.check_if_guest_can_checkout())

    def test_checkout_guest(self):
        self.guest_06.checking_out_guest()
        self.assertEqual("checked-out", self.guest_06.status)

# Guest Wallet
    def test_check_guest_wallet(self):
        self.assertEqual(12.00, self.guest_02.wallet)
        
# Guest Favourite Song
    def test_check_guest_fav_song(self):
        self.assertEqual("Roxanne", self.guest_02.favourite_song)
    
# Guest disliked artist
    def test_check_guest_disliked_artist(self):
        self.assertEqual("Madonna", self.guest_15.disliked_artist)

# Guest reaction to song
    def test_guest_likes_the_song(self):
        self.guest_08.guest_likes_the_song()
        self.assertEqual("Oh Yeah!", self.guest_08.guest_likes_the_song())

    def test_guest_doesnt_like_the_song(self):
        self.guest_06.guest_doesnt_like_the_song()
        self.assertEqual("I will skip this one", self.guest_06.guest_doesnt_like_the_song())