import random

from itertools import cycle


def get_num_sticks():
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
    while True:
        num = input("How many players (2 - 10), including CPU players: ")
        if num.isdigit() and 2 <= int(num) <= 6:
            return int(num)
        print("Looking for a number between 2 and 10.")


def get_name(number):
    player_type = '0'
    prefix = ['Mr', 'Mrs', 'Ms', 'Dr']
    while player_type not in ('1', '2'):
        player_type = input("Player {} is:\n1. Human\n2. CPU\n>>> ".format(number))
        if player_type not in ('1', '2'):
            print("Please type 1 for human or 2 for CPU.")
        if player_type == '1':
            player_name = input("Player {}'s name: ".format(number))
        else:
            player_name = '{}. Bot{}'.format(random.choice(prefix), number)
    return {'Name': player_name, 'Type': player_type}


def get_players():
    players = {}
    num_players = get_number_of_players()
    for player in range(1, num_players + 1):
        name = get_name(player)
        players[player] = name
    return players


def player_turn(player):
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


def play(sticks, players):
    player_list = [x['Type'] + x['Name'] for x in players.values()]
    # http://stackoverflow.com/questions/21884119/how-to-alternate-between-two-players
    for player in cycle(player_list):
        player_name = player[1:]
        player_type = player[:1]
        if sticks == 1:
            print("\nLast stick, have fun...")
        else:
            print("\nThere are {} stick(s) on the board.".format(sticks))
        if player_type == '1':
            pick = player_turn(player_name)
        else:
            pick = random.choice([1, 3])
            print("{} picked {} sticks.".format(player_name, pick))
        if pick > sticks:
            continue
        sticks -= pick
        if sticks == 0:
            print("\n{}, you lose.".format(player_name))
            break


def main():
    print("Welcome to the Game of Sticks!")
    play(get_num_sticks(), get_players())


if __name__ == '__main__':
    main()
