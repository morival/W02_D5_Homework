class Room:
    
    def __init__(self, name, capacity, entry_fee, checked_in_guests, assigned_songs):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.checked_in_guests = checked_in_guests
        self.assigned_songs = assigned_songs
        self.income_records = 0
        self.special_requests = []