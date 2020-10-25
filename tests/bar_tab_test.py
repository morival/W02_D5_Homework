import unittest
from classes.bar_tab import BarTab

class TestBarTab(unittest.TestCase):

    def setUp(self):

        self.menu = [
            {
                "name": "Ya Danger",
                "price": 9.00,
                "ingredients": ["Hendrick’s Orbium", "Fino", "Queen Olive", "Pineapple"]
            },
            {
                "name": "Red Panda",
                "price": 9.00,
                "ingredients": ["Tanqueray", "Lemon", "Tomato", "Sriracha", "Kaffir Lime Leaf", "Cucumber", "Guinness Foam", "Worcestershire Sauce"]
            },
            {
                "name": "Switched Negroni",
                "price": 9.00,
                "ingredients": ["Citrus Star of Bombay", "Cocchi Torino", "Campari"]
            },
            {
                "name": "Birdcage",
                "price": 9.50,
                "ingredients": ["Johnnie Walker Gold Label", "Aperol", "Angostura Bitters", "Rhubarb & Lemongrass Shrub", "Cinnamon & Clove Smoke"]
            }
        ]
        self.bar_tab_01 = BarTab("Cocktail Bar", self.menu, [])


    # Bar Name
    def test_bar_tab_has_name(self):
        self.assertEqual("Cocktail Bar", self.bar_tab_01.name)

    # Menu
        # Check Drink Name
    def test_drink_name(self):
        self.assertEqual("Red Panda", self.bar_tab_01.check_drink_name(self.bar_tab_01.menu, "Red Panda"))

        # Check if Drink is in Menu and Show the Price
    def test_check_drink_price(self):
        self.assertEqual(9.50, self.bar_tab_01.check_drink_price(self.bar_tab_01.menu, "Birdcage"))

    def test_if_drink_not_in_menu(self):
        self.assertEqual("This drink is not available", self.bar_tab_01.check_drink_price(self.bar_tab_01.menu, "Sex on the Beach"))
    
        # Check the Ingrediets of the Drink
    def test_check_drink_ingredients(self):
        self.assertEqual(["Citrus Star of Bombay", "Cocchi Torino", "Campari"], self.bar_tab_01.check_drink_ingredients(self.bar_tab_01.menu, "Switched Negroni"))


        