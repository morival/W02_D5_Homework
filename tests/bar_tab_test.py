import unittest
from unittest.case import TestCase
from classes.bar_tab import BarTab

class TestBarTab(unittest, TestCase):

    def setUp(self):

        self.bar_tab_01 = BarTab("Cocktail Bar", self.menu, 0)

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

        