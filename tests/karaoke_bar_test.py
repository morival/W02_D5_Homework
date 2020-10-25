import unittest

from classes.guest import *
from classes.room import *
from classes.song import *
from classes.karaoke_bar import *

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        
    # Guests
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

    # Rooms
        self.room_01 = Room("Rock Room", 5, 10.00, [], [], {})
        self.room_02 = Room("Reggae Room", 4, 12.00, [], [], {})
        self.room_03 = Room("\'80s Room", 6, 15.00, [], [], {})

    # Songs
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
        self.rock_songs = [self.song_01, self.song_02, self.song_03, self.song_04, self.song_05, self.song_06, self.song_07]
        self.reggae_songs = [self.song_08, self.song_09, self.song_10, self.song_11, self.song_12, self.song_13, self.song_14]
        self.eighties_songs = [self.song_15, self.song_16, self.song_17, self.song_18, self.song_19, self.song_20, self.song_21]
        
# Karaoke Bar
        self.karaoke_bar = KaraokeBar(self.guest_01, self.room_01, self.song_05, "Screeching Seagull")


    def test_bar_has_name(self):
        self.assertEqual("Screeching Seagull", self.karaoke_bar.bar_name)
    
# Guests
    # List of Guests
    def test_check_number_of_guests_in_list_while_empty(self):
        self.assertEqual(0, self.karaoke_bar.guest_count())
        
        # add
    def test_add_guest_to_list(self):
        self.karaoke_bar.add_guest_to_list(self.guest_01)
        self.assertEqual(1, self.karaoke_bar.guest_count())
        self.assertEqual("John Stone", self.karaoke_bar.list_of_guests[0].name)

        # remove
    def test_remove_guest_from_list(self):
        self.karaoke_bar.add_guest_to_list(self.guest_01)
        self.karaoke_bar.remove_guest_from_list(self.guest_01)
        self.assertEqual(0, self.karaoke_bar.guest_count())

    # Check-in Check-out
        # Check-in Guest to Room that is on the List
    def test_add_guest_to_room_on_list(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.assertEqual("John Stone", self.karaoke_bar.list_of_rooms[0].checked_in_guests[0].name)
        self.assertEqual("checked-in", self.karaoke_bar.list_of_rooms[0].checked_in_guests[0].status)

        # Not allowed multiple check-in of the same person to the same room
    def test_multi_check_in_same_guest_not_allowed(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.assertEqual(1, len(self.room_01.checked_in_guests))

        # Check-in Guest to First Free Room and Pay Entry Fee
    def test_add_guest_to_first_free_room_and_pay(self):
        full_room = Room("Rock Room", 5, 10.00, ["g1", "g2", "g3", "g4", "g5"], [], {})
        self.karaoke_bar.add_room_to_list(full_room)
        self.karaoke_bar.add_room_to_list(self.room_02)
        self.karaoke_bar.add_room_to_list(self.room_03)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.assertEqual("John Stone", self.karaoke_bar.list_of_rooms[1].checked_in_guests[0].name)
        self.assertEqual(0, len(self.karaoke_bar.list_of_rooms[2].checked_in_guests))
        self.assertEqual(38, self.karaoke_bar.list_of_rooms[1].checked_in_guests[0].wallet)

        # Check when all Rooms are Full
    def test_all_rooms_full(self):
        full_room = Room("Rock Room", 5, 10.00, ["g1", "g2", "g3", "g4", "g5"], [], {})
        self.karaoke_bar.add_room_to_list(full_room)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.assertEqual("All rooms are full. Please try later.", \
            self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms))

        # Check when Guest does not have enough Money to Pay Entry Fee
    def test_guest_no_funds_for_entry_fee(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.assertEqual("Sorry. You don't have enough money to get in.", \
            self.karaoke_bar.guest_check_in_free_room(self.guest_12, self.karaoke_bar.list_of_rooms))

        # Check-out from room
    def test_guest_check_out_from_room(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.karaoke_bar.guest_check_out_from_room(self.guest_01, self.room_01)
        self.assertEqual(0, len(self.room_01.checked_in_guests))

# Rooms
    # List of Rooms
        # Check Number of Rooms on List before Adding
    def test_check_number_of_rooms_on_list_while_empty(self):
        self.assertEqual(0, self.karaoke_bar.room_count())
    
        # Add Room to List
    def test_add_room_to_list(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.assertEqual(1, self.karaoke_bar.room_count())
        self.assertEqual("Rock Room", self.karaoke_bar.list_of_rooms[0].name)

        # Remove Room from List
    def test_remove_room_from_list(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.remove_room_from_list(self.room_01)
        self.assertEqual(0, self.karaoke_bar.room_count())

    #  List of Assigned Songs
        # Assign to Room
    def test_assign_song_to_room(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.assign_song(self.song_05, self.karaoke_bar.list_of_rooms[0])
        self.assertEqual("Kashmir", self.room_01.assigned_songs[0].title)
        self.assertEqual(1, len(self.karaoke_bar.list_of_rooms[0].assigned_songs))
        
        # Not allowed repeating Songs in Room
    def test_multi_assign_same_song_not_allowed(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.assign_song(self.song_05, self.karaoke_bar.list_of_rooms[0]) # checking different way of accessing the element in nested list 
        self.karaoke_bar.assign_song(self.song_05, self.karaoke_bar.list_of_rooms[0])        
        self.karaoke_bar.assign_song(self.song_05, self.room_01)
        self.assertEqual(1, len(self.room_01.assigned_songs))

        # Remove Song from Room
    def test_remove_song_from_room(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.assign_song(self.song_05, self.karaoke_bar.list_of_rooms[0]) 
        self.karaoke_bar.remove_song(self.song_05, self.room_01)
        self.assertEqual(0, len(self.room_01.assigned_songs))
    
    # Guest Reaction to Song/Artist
        # Positive
    def test_guest_likes_the_song(self):
        self.karaoke_bar.reaction_to_songs(self.guest_01, self.rock_songs)
        self.assertEqual("Whoo!", self.karaoke_bar.reaction_to_songs(self.guest_01, self.rock_songs))

        # Negative
    # def test_guest_doesnt_like_the_song(self):
        self.karaoke_bar.reaction_to_songs(self.guest_03, self.rock_songs)
        self.assertEqual("I will skip this one", self.karaoke_bar.reaction_to_songs(self.guest_03, self.rock_songs))

    # Payments
        # Entry Fee
    def test_guest_pays_entry_fee(self):
        self.karaoke_bar.add_room_to_list(self.room_01)
        self.karaoke_bar.guest_check_in_free_room(self.guest_01, self.karaoke_bar.list_of_rooms)
        self.assertEqual(40.00, self.karaoke_bar.list_of_rooms[0].checked_in_guests[0].wallet)