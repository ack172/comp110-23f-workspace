"""Defining a class!"""


# think of a class definition as a 'roadmap' for objects that belong to the class
# you are definining the underlying structure every instance of this class would 

class Pizza:
    """This is my class to represent pizza."""
    # attributes
    # syntax <name> : <type>
    # below are the attributes. Every pizza we make will have a size, toppings, gluten_free
    size: str
    toppings: int
    gluten_free: bool 

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool) -> ():
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # returns self

    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1
        return cost
    
    def add_toppings(self, num_toppings: int):
        """update existing pizza order with num_toppings"""
        self.toppings += num_toppings