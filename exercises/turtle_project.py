"""Programming a solar system using turtle."""

__author__ = "730385079"

from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    turtlez: Turtle = Turtle()
    # drawing background (black for outer space)
    draw_square(turtlez, -400, 400, 1000, "black", "black")
    """Above and beyond- trying something fun! Described in comments below."""
    # establishing indexes for x and y coordinates for stars
    # prints stars all over the scene background
    star_idx1: int = -400
    star_idx2: int = -400

    while star_idx1 <= 400:
        star_idx2 = -400
        while star_idx2 <= 400:
            draw_star(turtlez, star_idx1, star_idx2, 6)
            star_idx2 += 150
        star_idx1 += 150

    draw_planet(turtlez, -150, -230, 40, "red", "red")
    draw_planet(turtlez, 200, 200, 50, "blue", "blue")
    draw_gas_giant(turtlez, -90, 60, 80)
    turtlez.hideturtle()
    done()


def draw_star(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a star of the given width whose top-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.pencolor("purple")
    a_turtle.fillcolor("yellow")
    a_turtle.begin_fill()

    i: int = 0
    while i < 5:
        a_turtle.forward(width)
        a_turtle.right(120)
        a_turtle.forward(width)
        a_turtle.right(-48)
        i += 1
    a_turtle.end_fill()


def draw_planet(a_turtle: Turtle, x_planet: float, y_planet: float, width: float, color: str, penoutlinecolor: str) -> None:
    """Draws a circle with variable width at given coordinates. Meant to represent planets."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x_planet, y_planet) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()

    a_turtle.pencolor(penoutlinecolor)
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()

    a_turtle.circle(width)
    a_turtle.end_fill()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float, pen_color: str, fill_color: str) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    
    a_turtle.pencolor(pen_color)
    a_turtle.fillcolor(fill_color)
    a_turtle.begin_fill()

    # using an index and a while loop to draw the 4 sides of the square
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def draw_gas_giant(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a gas giant planet, with different colors located within it to show gas pockets."""
    """Above and Beyond- using component functions. Using Draw Planet function to draw gas giant planet"""
    # Above and beyond- using component functions
    # big planet
    draw_planet(a_turtle, x, y, width, "skyblue", "skyblue")
    # gas craters, programmed as smaller circles with variations on coordinates to put them in random spots
    draw_planet(a_turtle, x - 16, y + 15, width / 25, "blue", "white")
    draw_planet(a_turtle, x - 25, y + 45, width / 30, "purple", "white")
    draw_planet(a_turtle, x + 13, y + 55, width / 15, "blue", "white")
    draw_planet(a_turtle, x + 30, y + 80, width / 20, "navy", "white")
    draw_planet(a_turtle, x + 40, y + 90, width / 12, "purple", "white")
    draw_planet(a_turtle, x - 40, y + 97, width / 7, "blue", "white")
    draw_planet(a_turtle, x - 30, y + 57, width / 10, "navy", "white")
    draw_planet(a_turtle, x + 37, y + 13, width / 9, "purple", "white")


if __name__ == "__main__":
    main()