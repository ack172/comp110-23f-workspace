"""File to define River class."""

__author__ = "730385079"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to represent river."""
    day: int 
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bears."""
        list1: list[Bear] = []
        list2: list[Fish] = []
        for bear in self.bears:
            if bear.age <= 5:
                list1.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                list2.append(fish)
        self.fish = list2
        self.bears = list1
        return None
    
    def check_hunger(self):
        """Checking hunger levels of bears."""
        bear_list: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score < 0:
                bear_list.append(elem)
        self.bears = bear_list
        return None
        
    def repopulate_fish(self):
        """Method to repopulate fish."""
        fish_repopulation_number: int = (4 * (len(self.fish) // 2))
        for elem in range(0, fish_repopulation_number):
            fish_repopulation = Fish()
            self.fish.append(fish_repopulation)
        return None
    
    def repopulate_bears(self):
        """Method to repopulate bears."""
        bear_repopulation_number: int = len(self.bears) // 2
        for elem in range(0, bear_repopulation_number):
            bear_repopulation = Bear()
            self.bears.append(bear_repopulation)
        return None
    
    def view_river(self):
        """Method to view the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
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

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Method to remove amount of many fish from the river."""
        for elem in range(0, amount):
            self.fish.pop(elem)

    def bears_eating(self):
        """Bears will eat fish if there are more than 5 in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None


            
