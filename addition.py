#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program adds 2 integer numbers


def main():
    # This function adds 2 integer numbers

    # Input
    number1 = int(input("Please enter the first number(integer): "))
    number2 = int(input("Please enter the second number(integer): "))

    # process
    total = number1 + number2

    # output
    print("the calculated number is: {}".format(total))


if __name__ == "__main__":
    main()
