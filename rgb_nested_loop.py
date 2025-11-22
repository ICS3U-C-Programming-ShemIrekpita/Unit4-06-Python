#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/22/2025
# This program generates a random RGB colour when the user types "GO"

import random

# Constant that stores the required user input
GEN_NUM1 = "GO"
GEN_NUM2 = "Go"
GEN_NUM3 = "go"


def main():
    # Generate three random numbers between 0 and 255 for RGB
    colour_1 = random.randint(0, 255)
    colour_2 = random.randint(0, 255)
    colour_3 = random.randint(0, 255)
    while True:
        # Ask the user to type "GO" to reveal the random colour
        key = "RGB Color Codes Chart"
        key = input("Type GO to generate a random colour: ")
        # Check if the user typed "GO"
        if key == GEN_NUM1 or key == GEN_NUM2 or key == GEN_NUM3:
            # Display RGB values
            print("R", colour_1)
            print("G", colour_2)
            print("B", colour_3)
            # Ending message + cute ASCII art
            print("Thank you for playing")
            print(" /\\_/\\  ")
            print("( ^_^ )")
            print(" > ^ < ")
            break  # Stop the loop
        else:
            # User typed something other than "GO"
            print("You have to type in the GO to get a colour")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
