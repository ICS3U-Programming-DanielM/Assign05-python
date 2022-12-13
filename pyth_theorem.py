#!/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Dec. 12, 2022
# This program uses a do while loop to
# ask user if they want to solve
# hypotenuse, opposite or adjacent. then calculates the answer
# and then asks if the want to continue or not.
import math


# makes a function to calculate hypotenuse
def calc_hyp(adj, opp):
    # calculates hypotenuse if asked
    sum = adj**2 + opp**2
    hypotenuse = math.sqrt(sum)
    # returns hypotenuse to main
    return hypotenuse


# makes a function that calculates the opposite
def calc_opp(hyp, adj):
    # calculates opposite if asked
    sum = hyp**2 - adj**2
    opposite = math.sqrt(sum)
    # returns the opposite to main
    return opposite


# makes a function to calculate the adjacent
def calc_adj(hyp, opp):
    # calculates adjacent if asked
    sum = hyp**2 - opp
    adjacent = math.sqrt(sum)
    # returns the adjacent to main
    return adjacent


# calls the functions and displays the call.
def main():
    # displays opening message to user.
    print("")
    print("Welcome to the pythagorean theorem calculator.")
    # uses loop to ask user if they want to continue or
    # end at the beginning and end of the question
    while True:
        # Asks user if they want to continue at
        # the beginning and the end.
        print("")
        print("Do you wish to continue?")
        # asks user to input Y for yes and N for no
        # caps only
        ask_continue = input("Enter (Y) for yes or (N) for no: ")
        try:
            # checks to make sure that user input is a string
            ask_cont = str(ask_continue)
            # checks to see if user input is a capital Y
            # if it is capital Y then it
            # continues to the rest of the code
            if ask_cont == "Y":
                print("")
                print("This calculator solves for either")
                print("hypotenuse, opposite or adjacent")
                print("Enter hyp for hypotenuse")
                print("opp for opposite and")
                print("adj for adjacent")
            # checks to see if user input is a capital N
            # if it is capital N then it prints
            # the message and ends the program
            elif ask_cont == "N":
                print("Thanks for using the pythagorean theorem calculator")
                break
            # if it neither then it displays the
            # message ans loops back to get user input
            else:
                print("Invalid input, you can only enter (Y) or (N)")
                print("")
                continue
        # if it not a string then it tells user it is an invalid input
        # and loops back to get user input
        except Exception:
            print("{0} is an invalid input".format(ask_continue))
            continue
        # uses a do while loop to loop
        # back if user input is invalid
        # or if hypotenuse is less than adjacent or opposite
        while True:
            # asks user what they want to calculate either
            # hypotenuse, adjacent and opposite.
            Ask_user = input("Enter what you would like to calculate: ")
            # checks to see if user input is hyp or not.
            if Ask_user == "hyp":
                # tells user what the chose
                print("You chose Hypotenuse")
                print("")
                # asks user to input the adjacent and opposite
                adj_input = input("Enter the adjacent number: ")
                opp_input = input("Enter the opposite number: ")
                try:
                    # converts user input from string to integer
                    adj_user = float(adj_input)
                    try:
                        opp_user = float(opp_input)
                        # makes sure user number is bigger than zero
                        if adj_user < 0 or opp_user < 0:
                            print("Your input is lower than 0")
                            continue
                        else:
                            # calls the functions and displays it to user
                            hypotenuse_user = calc_hyp(adj_user, opp_user)
                            print("")
                            print(
                                "The hypotenuse is equal to {:.2f}".format(
                                    hypotenuse_user
                                )
                            )
                            break
                    # checks to see if opp_user is an integer
                    except Exception:
                        print("{0} is not a valid number.".format(opp_input))
                        break
                # checks to see if adj_user is an integer
                except Exception:
                    print("{0} is not a valid number.".format(adj_input))
                    break
            # if user input is opp the continue with this part of the code
            elif Ask_user == "opp":
                print("You chose Opposite")
                print("")
                # Ask user to enter hypotenuse and adjacent
                hyp_input = input("Enter the Hypotenuse number: ")
                adj_input = input("Enter the adjacent number: ")
                try:
                    # change user input to a integer
                    hyp_user = float(hyp_input)
                    try:
                        # change user input to a integer
                        adj_user = float(adj_input)
                        # makes sure user input isn't lower than 0
                        if adj_user < 0 or hyp_user < 0:
                            print("Your input is lower than 0")
                            continue
                        # makes sure hypotenuse is lower than adjacent
                        if hyp_user < adj_user:
                            print("Hypotenuse cannot be less adjacent")
                            print("")
                            continue
                        # calls the the opposite function
                        # and displays it to user
                        opposite_user = calc_opp(hyp_user, adj_user)
                        print("")
                        print("The opposite is equal to {:.2f}".format(opposite_user))
                        break
                    # if user input isn't a integer display to user
                    except Exception:
                        print("{0} is not a valid number.".format(adj_input))
                        break
                # if user input isn't a integer then display to user
                except Exception:
                    print("{0} is not a valid number.".format(hyp_input))
                    break
            # if user input was adj then continue with this part
            # of the code
            elif Ask_user == "adj":
                # display what user chose to user
                print("You chose Adjacent")
                print("")
                # Ask user for input
                hyp_input = input("Enter the Hypotenuse number: ")
                opp_input = input("Enter the Opposite number: ")
                try:
                    # changes hyp_input to a integer
                    hyp_user = float(hyp_input)
                    try:
                        # changes opp_input to a integer
                        opp_user = float(opp_input)
                        # makes sure user input isn't lower than 0
                        if hyp_user < 0 or opp_user < 0:
                            print("Your input is lower than 0")
                            continue
                        # makes sure hyp_user isn't lower than 0
                        if hyp_user < opp_user:
                            print("Hypotenuse cannot be less opposite")
                            continue
                        # calls adjacent and displays the calculation
                        adjacent_user = calc_opp(hyp_user, opp_user)
                        print("")
                        print("The opposite is equal to {:.2f}".format(adjacent_user))
                        break
                    # if user input isn't an integer then
                    # display to user
                    except Exception:
                        print("{0} is not a valid number.".format(opp_input))
                        break
                # if user input isn't an integer then
                # display to user
                except Exception:
                    print("{0} is not a valid number.".format(hyp_input))
                    break
            # if user input isn't hyp, opp or adj
            # then display to user
            else:
                print("You can't solve for {0}".format(Ask_user))
                continue


if __name__ == "__main__":
    main()
