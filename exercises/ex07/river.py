"""File to define River class."""

__author__ = "730648283"

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self):
        """remove fish older 3 and bears older 5"""
        survive_fish = []
        survive_bear = []
        # make empty list here
        for fish in self.fish:
            if fish.age <= 3:
                survive_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                survive_bear.append(bear)
        # TA question; now change self.bear/fish to equal new list
        # so no errors
        self.fish = survive_fish
        self.bears = survive_bear
        return None

    def remove_fish(self, amount: int):
        """remove FIRST amount of fish from river"""
        count = 0
        while count < amount and self.fish:
            self.fish.pop(0)
            count += 1
        # is there any other way to use this w/o using and??? Ive
        # tried a bunch and cant find another way
        return None

    def bears_eating(self):
        """check 5 fish, if then bear eats 3 fish each"""
        for bear in self.bears:
            if len(self.fish) >= 5:  # needs at least 5 fish
                self.remove_fish(3)  # take out 3 fish
                bear.eat(3)  # each bear eats 3
        return None

    def check_hunger(self):
        """take out bear hunger score < 0"""
        # this is check for starving
        survive_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survive_bears.append(bear)
        self.bears = survive_bears  # same as before, replace list
        return None

    def repopulate_fish(self):
        """2 fish makes 4 fish babies"""
        new_fish = (len(self.fish) // 2) * 4  # new concept! int division/whole num
        count = 0
        while count < new_fish:
            self.fish.append(Fish())  # TA help -  basically call fish to
            # instance and add new fish using append
            count += 1
        return None

    def repopulate_bears(self):
        """2 bears makes +1 bear"""
        new_bears = len(self.bears) // 2  # new concept! int division/whole num
        count = 0
        while count < new_bears:
            self.bears.append(Bear())  # TA help -  basically call bear to
            # instance and add new bear using append
            count += 1
        return None

    def view_river(self):
        """print the vals for the river"""
        # want to use f strings or concat here
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
        return None

    def one_river_week(self):
        """simulate one week of life on the river"""
        days: int = 7
        while days > 0:
            self.one_river_day()
            days -= 1
        # this set up basically does one day each and
        # then dec the count of days
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None
