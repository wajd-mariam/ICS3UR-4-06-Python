# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program calculates all possible combos for RGB colors


def main():
    # this function uses a nested loop

    # process & output
    for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB: (" + str(red) + ", " + str(green) + ", " +
                      str(blue) + ")")


if __name__ == "__main__":
    main()
