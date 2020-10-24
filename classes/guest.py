class Guest:

    def __init__(self, name, status, wallet, favourite_song, hated_genre):
        self.name = name
        self.status = status
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.hated_genre = hated_genre

    def check_if_guest_can_checkin(self):
        if self.status == "waiting":
            return True
        else:
            return False

    def checking_in_guest(self):
        if self.check_if_guest_can_checkin() == True:
            self.status = "checked-in"

    def check_if_guest_can_checkout(self):
        if self.status == "checked-in":
            return True
        else:
            return False

    def checking_out_guest(self):
        if self.check_if_guest_can_checkout() == True:
            self.status = "checked-out"