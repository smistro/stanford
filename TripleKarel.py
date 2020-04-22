from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    block_one()

    while left_is_blocked():
        put_beeper()
        move()
    turn_right()

    block_two()




    """From this point on, the functions used to create the building
    blocks above will be defined. Awesome. Many thanks to Stanford University
    for providing me with this unique and challenging learning experience.
    I'am just grateful for this opportunity."""
# Defines the most used command by Karel
def primary_function():
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
    move()

# Defines secondary command
def secondary_function():
    while left_is_blocked():
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move()

# Defines tertiary function
def tertiary_function():
    while left_is_blocked():
        put_beeper()
        move()
    turn_right()
    put_beeper()
    move()

# Defining the building blocks
def block_one():
    primary_function()
    primary_function()
    secondary_function()
    primary_function()
    primary_function()

def block_two():
    primary_function()
    primary_function()
    primary_function()
    tertiary_function()
    tertiary_function()
    primary_function()



# Turns Karel 90 degrees to the right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Turns Karel around 180 degrees.
def turn_around():
    turn_left()
    turn_left()



    pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
