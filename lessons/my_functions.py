"""Things I'll be importing."""

def addition(x: int, y: int)-> int:
    return x + y

my_variable: str = "hello!"

if __name__ == "__main__":
    print("This should only print when runnning my functions.")
else:
    print("my functions is being imported.")