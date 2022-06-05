#!/usr/bin/env python3
import random


def check_user_imput(input):
    valid_input = ["R", "P", "S"]

    return input in valid_input


def computer_choice():
    valid_input = ["R", "P", "S"]

    return random.choice(valid_input)


def check_winner(user, ia):
    msg_ia_win = "CPU win !!!!"
    msg_user_win = "Player win !!!!"
    msg_tie = "Moufff, it's a tie !!!!"

    if user == "R" and ia == "P":
        print(msg_ia_win)
        return True
    elif user == "R" and ia == "S":
        print(msg_user_win)
        return True
    elif user == "R" and ia == "R":
        print(msg_tie)
        return False
    elif user == "P" and ia == "R":
        print(msg_user_win)
        return True
    elif user == "P" and ia == "S":
        print(msg_ia_win)
        return True
    elif user == "P" and ia == "P":
        print(msg_tie)
        return False
    elif user == "S" and ia == "P":
        print(msg_user_win)
        return True
    elif user == "S" and ia == "R":
        print(msg_ia_win)
        return True
    else:
        print(msg_tie)
    return False


def game_loop():
    valid_cmd = {"P": "Paper", "R": "Rock", "S": "Scissors"}
    print("Welcome to Rock-Paper-Scissors game !!!!\n")
    while True:
        print("Hey user, choose between \"R\" \"P\" \"S\" ")
        user_choice = input()
        if not check_user_imput(user_choice):
            print("Wrong command \n")
            continue
        result = computer_choice()
        print("\n(Player ({}) : CPU ({}))\n".format(
            valid_cmd[user_choice], valid_cmd[result]))
        if check_winner(user_choice, result):
            break
        else:
            continue
    return 0


game_loop()
