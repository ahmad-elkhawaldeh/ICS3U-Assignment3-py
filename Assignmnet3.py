# !/user/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
# This program will get
# a number from the user and displays that name of the weekday


def main():
    # this function checks if the user puts the right number for a specific day

    # input
    user_input = int(input("enter a number from 1 to 7:"))

    # process/  # output
    if user_input == 1:
        print(" the wekkday is sunday   ")
    elif user_input == 2:
        print(" the weekday is monday ")
    elif user_input == 3:
        print(" the weekday is tuesday ")
    elif user_input == 4:
        print(" the weekday is wedneday ")
    elif user_input == 5:
        print(" the weekday is thursday ")
    elif user_input == 6:
        print(" the weekday is friday ")
    elif user_input == 7:
        print(" the weekday is saturday ")
    else:
        print(" there is no weekday for the following number")

    if __name__ == "__main__":
        main()
