import pickle
import random

from itertools import cycle


def load_ai_dict():
    """Uses pickle to load the ai's dictionary file."""
    with open('ai_guesses.pickle', 'rb') as handle:
        return pickle.load(handle)


def save_ai_dict(ai_dict):
    """Saves the updated ai_dict after a game ends."""
    with open('ai_guesses.pickle', 'wb') as handle:
        pickle.dump(ai_dict, handle)


def get_num_sticks():
    """Gets player to input a number between 10 and 100."""
    while True:
        try:
            sticks = int(input("How many sticks are there on the table initially (10-100)? "))
        except ValueError:
            print("That's not a number!\n")
        else:
            if 10 <= sticks <= 100:
                return sticks
            else:
                print("Need a number between 10 and 100 please.\n")


def get_number_of_players():
    """Ensures that the player picks between 2 and 5 players."""
    while True:
        num = input("How many players (2 - 5), including CPU players: ")
        if num.isdigit() and 2 <= int(num) <= 5:
            return int(num)
        print("Looking for a number between 2 and 10.")


def get_name(number):
    """
    Program keeps track of players and their types (human or CPU) by
    returning a dictionary here from the user's input.
    Bots are given a prefix to human them up a little.
    """
    player_type = '0'
    prefix = ['Mr', 'Mrs', 'Ms', 'Dr']
    while player_type not in ('1', '2'):
        player_type = input("\nPlayer {} is:\n1. Human\n2. CPU\n>>> ".format(number))
        if player_type not in ('1', '2'):
            print("Please type 1 for human or 2 for CPU.")
        if player_type == '1':
            player_name = input("Player {}'s name: ".format(number))
        else:
            player_name = '{}. Bot{}'.format(random.choice(prefix), number)
    return {'Name': player_name, 'Type': player_type}


def get_players():
    """
    Loops through the range of players entered, and gets a name. The
    number in the loop is used to give each player uniqueness to help
    track them through the rest of the game. What's returned is a dict
    with the number in the loop as the key, and another dictionary
    that stores the name and the type of player (human/computer).
    """
    players = {}
    num_players = get_number_of_players()
    for player in range(1, num_players + 1):
        name = get_name(player)
        players[player] = name
    return players


def player_turn(player):
    """Ensures user enteres a valid number of sticks to pick up."""
    while True:
        try:
            selection = int(input("{}: How many sticks do you take (1-3)? ".format(player)))
        except ValueError:
            print("That's not a number!\n")
        else:
            if 1 <= selection <= 3:
                return selection
            else:
                print("Need a number between 1 and 3 please.\n")


def update_ai_dict(player_type, ai_dict, ai_picks):
    """
    This function see which player won (human or computer) to make
    the correct update to the ai_dict that's stored as a pickle file.
    """
    if player_type == '2':
        for k, v in ai_picks.items():
            if k in (1, 2):
                continue
            elif len(ai_dict[k]) > 1:
                ai_dict[k].remove(v)
            else:
                ai_dict[k] = [(random.choice([1, 2, 3]))]
    else:
        for k, v in ai_picks.items():
            ai_dict[k].append(v)

    return ai_dict


def check_pick(sticks, pick):
    if pick <= sticks:
        return True


def play(sticks, players):
    player_list = [x['Type'] + x['Name'] for x in players.values()]
    ai_dict = load_ai_dict()
    ai_picks = {}
    # http://stackoverflow.com/questions/21884119/how-to-alternate-between-two-players
    for player in cycle(player_list):
        player_name = player[1:]
        player_type = player[:1]
        if sticks == 1:
            print("\nLast stick, have fun...")
        else:
            print("\nThere are {} stick(s) on the board.".format(sticks))
        if player_type == '1':
            while True:
                pick = player_turn(player_name)
                if check_pick(sticks, pick):
                    break
        else:
            while True:
                if sticks == 1:
                    pick = 1
                else:
                    pick = random.choice(ai_dict[sticks])
                if check_pick(sticks, pick):
                    break
            ai_picks[sticks] = pick
            print("{} picked {} sticks.".format(player_name, pick))
        sticks -= pick
        if sticks == 0:
            ai_dict = update_ai_dict(player_type, ai_dict, ai_picks)
            save_ai_dict(ai_dict)
            print("\n{}, you lose.\n\n".format(player_name))
            break


def main():
    while True:
        print("-" * 35)
        print("Welcome to the Game of Sticks!")
        player_choice = input("To play, press enter. To quit, enter 'Q'. ")
        if player_choice.upper() == 'Q':
            exit()
        play(get_num_sticks(), get_players())


if __name__ == '__main__':
    main()
