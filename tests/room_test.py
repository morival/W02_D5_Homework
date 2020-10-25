import unittest
from classes.room import Room
from classes.bar_tab import BarTab

class TestRoom(unittest.TestCase):

    def setUp(self):
    
    # Menu
        self.menu = [{
                "name": "Ya Danger",
                "price": 9.00,
                "ingredients": ["Hendrick’s Orbium", "Fino", "Queen Olive", "Pineapple"]
            }]
    # Bar
        self.bar_tab_01 = BarTab("Cocktail Bar", self.menu, {})

    # Rooms
        self.room_01 = Room("Rock Room", 5, 10.00, [], [], self.bar_tab_01)
        self.room_02 = Room("Reggae Room", 4, 12.00, [], [], self.bar_tab_01)
        self.room_03 = Room("\'80s Room", 6, 15.00, [], [], self.bar_tab_01)

    # Income Records


    # Room Name
    def test_check_room_name(self):
        self.assertEqual("Rock Room", self.room_01.name)

    # Room Capacity
    def test_check_room_capacity(self):
        self.assertEqual(4, self.room_02.capacity)

    # Room Entry Fee
    def test_check_room_entry_fee(self):
        self.assertEqual(15.00, self.room_03.entry_fee)

    # Room Checked-in Guests Number before adding elements
    def test_checked_in_guests(self):
        self.assertEqual(0, len(self.room_01.checked_in_guests))

    # Room Assigned Songs Number before adding elements
    def test_assigned_songs(self):
        self.assertEqual(0, len(self.room_02.assigned_songs))

    # Room has Income Records
    def test_room_income_records(self):
        self.assertEqual([], self.room_01.income_records)

    