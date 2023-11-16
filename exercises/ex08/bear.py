"""File to define Bear class."""


class Bear:
    """Modeling bears."""
    age: int
    hunger_score: int
    
    def __init__(self, init_age=0, init_hunger_score=0):
        """Constructor."""
        self.age = init_age
        self.hunger_score = init_hunger_score
        return None
    
    def one_day(self):
        """Method to model changes in bear's hunger scores and age per day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Method to reflect the amount of fish the bears eat in their hunger score."""
        self.hunger_score += num_fish