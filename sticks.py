from itertools import cycle


def get_num_sticks():
    while True:
        try:
            sticks = int(input("How many sticks are there on the table "
                               "initially (10-100)? "))
        except ValueError:
            print("That's not a number!\n")
        else:
            if 10 <= sticks <= 100:
                return sticks
            else:
                print("Need a number between 10 and 100 please.\n")


def player_turn(player):
    while True:
        try:
            selection = int(input("{}: How many sticks do you take "
                                  "(1-3)? ".format(player)))
        except ValueError:
            print("That's not a number!\n")
        else:
            if 1 <= selection <= 3:
                return selection
            else:
                print("Need a number between 1 and 3 please.\n")


def check_selection(sticks, pick):
    if pick > sticks:
        print("There are only {} sticks. Please try again.")
    else:
        return sticks - pick


def play(sticks):
    # http://stackoverflow.com/questions/21884119/how-to-alternate-between-two-players
    for player in cycle(["Player 1", "Player 2"]):
        print("\nThere are {} sticks on the board.".format(sticks))
        sticks = check_selection(sticks, player_turn(player))
        if sticks == 0:
            print("\n{}, you lose.".format(player))
            break


def main():
    print("Welcome to the Game of Sticks!")
    play(get_num_sticks())


if __name__ == '__main__':
    main()
