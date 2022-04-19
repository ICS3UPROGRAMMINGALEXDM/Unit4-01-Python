#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a number from the user and loops through every number
# up until you get to that number, then it calculates the sum of each number in between


def main():
    # Initializing variables
    u_num = input("Enter a positive number: ")
    loop_num = 0
    loop_sum = 0

    try:
        # converting to int
        u_num = int(u_num)

        # only continue if condition is met
        if u_num > 0:
            # used to loop through the number
            while loop_num < u_num:
                # adding one to the loop number
                loop_num += 1
                print("{} times through loop".format(loop_num))
                # updating the sum
                loop_sum += loop_num

            print("The sum of the numbers between 0-{0} is {1}".format(u_num, loop_sum))
        else:
            print("invalid input")

    except ValueError:
        print("Invalid Input")


if __name__ == "__main__":
    main()
