class KaraokeBar:
    
    def __init__(self, guest, room, song, bar_name):
        self.guest = guest
        self.room = room
        self.song = song
        self.bar_name = bar_name
        self.list_of_guests = []
        self.list_of_rooms = []
        self.list_of_songs = []
        
# Guests
    # Guest List
    def guest_count(self):
        return len(self.list_of_guests)

    def add_guest_to_list(self, new_guest):
        self.list_of_guests.append(new_guest)

    def remove_guest_from_list(self, guest):
        self.list_of_guests.remove(guest)

    # Check-in to Free Room
    def guest_check_in_free_room(self, guest, list_of_rooms):
        for room in list_of_rooms:
            if len(room.checked_in_guests) < room.capacity:
                if guest not in room.checked_in_guests:
                    return room.checked_in_guests.append(guest),\
                    guest.status.replace("waiting", "checked-in")
            elif len(room.checked_in_guests) == room.capacity:
                "All rooms are full. Please try later."

    # Check-out
    def guest_check_out_from_room(self, guest, room):
        if guest in room.checked_in_guests:
            room.checked_in_guests.remove(guest)

# Rooms
    # Room List
    def room_count(self):
        return len(self.list_of_rooms)

    def add_room_to_list(self, new_room):
        self.list_of_rooms.append(new_room)

    def remove_room_from_list(self, room):
        self.list_of_rooms.remove(room)

# Songs
    # Song List
    def song_count(self):
        return len(self.list_of_songs)

    def add_song_to_list(self, new_song):
        self.list_of_songs.append(new_song)

    def remove_song_from_list(self, song):
        self.list_of_songs.remove(song)

    # Assign Song
    def assign_song(self, song, room):
        if song not in room.assigned_songs:
            room.assigned_songs.append(song)

    # Remove Song
    def remove_song(self, song, room):
        if song in room.assigned_songs:
            room.assigned_songs.remove(song)

    