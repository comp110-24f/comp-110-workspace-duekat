"""File to define Bear class."""

__author__ = "730648283"


class Bear:

    def __init__(self):
        self.age = 1
        self.hunger_score = 0

        return None

    def one_day(self):
        """use as a simulator for bear age"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """inc the hunger score by fish eat"""
        self.hunger_score += num_fish
        return None
