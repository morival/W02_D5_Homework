import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_01 = Guest("John Stone", "checked-in", 50.00, "Kashmir", "\'80")
        self.guest_02 = Guest("Mia Wong", "waiting", 12.00, "Roxanne", "Techno")
        self.guest_03 = Guest("Natalie Lee-Walsh", "checked-out", 406.50, "O Carolina", "Pop")
        self.guest_04 = Guest("Ang Li", "waiting", 40.50, "O Carolina", "Classical")
        self.guest_05 = Guest("Nguta Ithya", "waiting", 36.50, "O Carolina", "Rock")
        self.guest_06 = Guest("Tamzyn French", "checked-in", 98.00, "O Carolina", "\'70")
        self.guest_07 = Guest("Salome Simoes", "checked-in", 27.20, "O Carolina", "Pop")
        self.guest_08 = Guest("Trevor Virtue", "waiting", 21.90, "O Carolina", "Heavy Metal")
        self.guest_09 = Guest("Eugenia Anders", "checked-out", 320.00, "O Carolina", "Rock")
        self.guest_10 = Guest("Tarryn Campbell-Gillies", "checked-in", 46.50, "O Carolina", "Trance")
        self.guest_11 = Guest("Andrew Kazantzis", "checked-out", 82.50, "O Carolina", "\'80")
        self.guest_12 = Guest("Verona Blair", "waiting", 6.50, "O Carolina", "Reggae")
        self.guest_13 = Guest("Jane Meldrum", "waiting", 116.30, "O Carolina", "Reggaeton")
        self.guest_14 = Guest("Maureen M. Smith", "checked-in", 12.70, "O Carolina", "Techno")
        self.guest_15 = Guest("Desiree Burch", "checked-in", 61.00, "O Carolina", "Pop")
        self.guest_16 = Guest("Daly Harry", "waiting", 47.80, "O Carolina", "Rock")


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
        self.guest_02.checkin_guest()
        self.assertEqual("checked-in", self.guest_02.status)

# Guest Wallet
    def test_check_guest_wallet(self):
        self.assertEqual(12.00, self.guest_02.wallet)
        
# Guest Favourite Song
    def test_check_guest_fav_song(self):
        self.assertEqual("Roxanne", self.guest_02.favourite_song)
    