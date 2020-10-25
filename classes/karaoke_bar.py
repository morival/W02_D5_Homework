class KaraokeBar:
    
    def __init__(self, guest, room, song, bar_name):
        self.guest = guest
        self.room = room
        self.song = song
        self.bar_name = bar_name
        self.list_of_guests = []
        self.list_of_rooms = []

        
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
            if len(room.checked_in_guests) < room.capacity: # check if the room is full
                if guest not in room.checked_in_guests: # check for dubplicated names
                    if guest.wallet >= room.entry_fee:              
                        guest.wallet -= room.entry_fee
                        guest.status ="checked-in"
                        return room.checked_in_guests.append(guest)
                    else:
                        return "Sorry. You don't have enough money to get in."
        return "All rooms are full. Please try later."

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

# Bar Tab
    # Guest can Afford Drink
    def guest_can_afford_drink(self, guest, drink_price):
        if guest.wallet >= drink_price:
            return True
        else:
            return False

    # Guest Pay for Drink at the Bar
    def guest_pay_for_drink(self, guest, drink_price):
        if self.guest_can_afford_drink(guest, drink_price) == True:
            guest.wallet -= drink_price
        return "Sorry. You don't have enough money to pay for this drink."

    # Add Money to Till
    def pay_to_till(self, drink_name, bar_tab, guest):
        bar_tab.till_records["item"] = drink_name
        bar_tab.till_records["price"] = self.check_drink_price(bar_tab.menu, drink_name)
        bar_tab.till_records["customer"] = guest.name

    # Register Transaction

# Songs
    # Assign Song to Room
    def assign_song(self, song, room):
        if song not in room.assigned_songs:
            room.assigned_songs.append(song)

    # Remove Song
    def remove_song(self, song, room):
        if song in room.assigned_songs:
            room.assigned_songs.remove(song)

    # Reaction to Song/Artist
    def reaction_to_songs(self, guest, list_of_songs):
        for song in list_of_songs:
            if guest.favourite_song == song.title:
                return "Whoo!"
            elif guest.disliked_artist == song.artist:
                return "I will skip this one"

