"""File to define Fish class."""


class Fish:
    """Modeling fish."""
    age: int

    def __init__(self, init_age=0):
        """Constructor."""
        self.age = init_age
        return None
    
    def one_day(self):
        """One day for the fish."""
        self.age += 1
        return None