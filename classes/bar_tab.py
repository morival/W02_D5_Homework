class BarTab:

    def __init__(self, name, menu, till_records):
        self.name = name
        self.menu = menu
        self.till_records = till_records

# Menu
    # Check Drink Name
    def check_drink_name(self, menu, order):
        for drink in menu:
            if drink["name"] == order:
                return drink["name"]
        return "This drink is not available"

    # Access Price of the Drink by Name
    def check_drink_price(self, menu, order):
        for drink in menu:
            if drink["name"] == order:
                return drink["price"]
        return "This drink is not available"

    # Access Ingredients of the Drink by Name
    def check_drink_ingredients(self, menu, order):
        for drink in menu:
            if drink["name"] == order:
                return drink["ingredients"]
        return "This drink is not vailable"

    