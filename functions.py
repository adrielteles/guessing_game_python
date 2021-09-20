import random
import config


# main game
def main_game():
    select_level()


def guessing_game_easy():
    # this game variables
    random_number = generate_random_number()

    while config.tentative_now <= config.tentative_easy:
        view_tentatives(config.tentative_now, config.tentative_easy)

        typed_number = int(input("Enter a number: "))
        if typed_number < 100:
            if random_number == typed_number:
                print("The number is", random_number, "You won", end="!")
                break
            if config.tentative_now == config.tentative_easy:
                print("You missed, Not have tentatives! Start a new game.")
                break
            if typed_number < random_number:
                print("You missed, Enter a larger number!")
            if typed_number > random_number:
                print("You missed, Enter a smaller number")
            if config.tentative_now == config.tentative_easy:
                print("One more tentative, Kep Calm")
        if typed_number > 100:
            print("erro this not a game scoop")

        config.tentative_now += 1


def guessing_game_hard():
    # this game variables
    random_number = generate_random_number()

    while config.tentative_now <= config.tentative_hard:
        view_tentatives(config.tentative_now, config.tentative_hard)

        typed_number = int(input("Enter a number: "))

        if typed_number < 100:
            if random_number == typed_number:
                print("The number is", random_number, "You won", end="!")
                break
            if config.tentative_now == config.tentative_hard:
                print("You missed, Not have tentatives! Start a new game.")
                break
            if typed_number < random_number:
                print("You missed, Enter a larger number!")
            if typed_number > random_number:
                print("You missed, Enter a smaller number")
            if config.tentative_now == config.tentative_hard:
                print("One more tentative, Kep Calm")
        if typed_number > 100:
            print("erro this not a game scoop")

        config.tentative_now += 1


def guessing_game_expert():
    # this game variables
    random_number = generate_random_number()

    while config.tentative_now <= config.tentative_expert:
        view_tentatives(config.tentative_now, config.tentative_expert)

        typed_number = int(input("Enter a number: "))

        if typed_number < 100:
            if random_number == typed_number:
                print("The number is", random_number, "You won", end="!")
                break
            if config.tentative_now == config.tentative_expert:
                print("You missed, Not have tentatives! Start a new game.")
                break
            if typed_number < random_number:
                print("You missed, Enter a larger number!")
            if typed_number > random_number:
                print("You missed, Enter a smaller number")
            if config.tentative_now == config.tentative_expert:
                print("One more tentative, Kep Calm")
            if typed_number > 100:
                print("erro this not a game scoop")

        config.tentative_now += 1


def guessing_game_brutal():
    # this game variables
    random_number = generate_random_number()

    while config.tentative_now <= config.tentative_brutal:
        view_tentatives(config.tentative_now, config.tentative_brutal)

        typed_number = int(input("Enter a number: "))

        if typed_number < 100:
            if random_number == typed_number:
                print("The number is", random_number, "You won", end="!")
                break
            if config.tentative_now == config.tentative_brutal:
                print("You missed, Not have tentatives! Start a new game.")
                break
            if typed_number < random_number:
                print("You missed, Enter a larger number!")
            if typed_number > random_number:
                print("You missed, Enter a smaller number")
            if config.tentative_now == config.tentative_brutal:
                print("One more tentative, Kep Calm")
        if typed_number > 100:
            print("erro this not a game scoop")

        config.tentative_now += 1


# this function generate a generic number for 1 and 100

def generate_random_number():
    random_number = int(random.randrange(1, 100))
    return random_number


# this function UI of tentative number

def view_tentatives(now, default):
    print("Tentative: ", now, "of", default)


# this function UI of select level difficulty

def select_level():
    print("Select game level")
    print("1.easy")
    print("2.hard")
    print("3.expert")
    print("4.brutal")
    print("-------------------------------")
    level = int(input("enter difficulty: "))

    if level == 1:
        guessing_game_easy()
    if level == 2:
        guessing_game_hard()
    if level == 3:
        guessing_game_expert()
    if level == 4:
        guessing_game_brutal()
    if level > 4:
        print("invalid level!")
