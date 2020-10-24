import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_01 = Room("Rock Room", 5, 10.00, [], [])
        self.room_02 = Room("Reggae Room", 4, 12.00, [], [])
        self.room_03 = Room("\'80s Room", 6, 15.00, [], [])

    # Room Name
    def test_check_room_name(self):
        self.assertEqual("Rock Room", self.room_01.name)

    # Room Capacity
    def test_check_room_capacity(self):
        self.assertEqual(4, self.room_02.capacity)

    # Room Entry Fee
    def test_check_room_entry_fee(self):
        self.assertEqual(15.00, self.room_03.entry_fee)

    