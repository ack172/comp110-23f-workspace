"""Instantistating a class."""

# import the class
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza() # constructor

# access/ set/ update attribute values
my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True
my_pizza.toppings += 2

print("Size: ")
print(my_pizza.size)

print(my_pizza)

sals_pizza: Pizza = Pizza()


def price(input_pizza: Pizza) -> float:
    """Function to compute the price of a pizza."""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 *input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1
    return cost

# calling function
print(price(my_pizza))

# calling method
print(my_pizza.price())