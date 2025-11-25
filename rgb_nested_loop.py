#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/22/2025
# This program generates a random RGB colour
def main():
    for r in range(0, 255, 1):
        for g in range(0, 255, 1):
            for b in range(0, 255, 1): 
                print(f"\033[38;2;{r};{g};{b}mRGB ({r}, {g}, {b})\033[0m")
    print("\nDone printing all RGB colours.")


if __name__ == "__main__":
    main()
