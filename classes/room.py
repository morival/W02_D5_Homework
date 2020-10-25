class Room:
    
    def __init__(self, name, capacity, entry_fee, checked_in_guests, assigned_songs, bar_tab):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.checked_in_guests = checked_in_guests
        self.assigned_songs = assigned_songs
        self.bar_tab = bar_tab
        self.income_records = []
        self.special_requests = []

    # Income Records
        # Income from Entry Fees
    