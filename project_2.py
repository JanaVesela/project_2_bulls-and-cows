"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jana Veselá
email: janca.vesela90@gmail.com


BULLS & COWS (Býci a Krávy)
==============================================================
Tento program simuluje hru Bulls and Cows, ve které uživatel
hádá čtyřciferná čísla a podle úspěšnosti (uhádnutí správné
číslice nebo její pozice) dostává zpětnou vazbu ve formě
bodového ohodnocení. 
"bulls" (býci), pokud uživatel uhodne jak číslo, tak jeho umístění 
"cows" (krávy), pokud uživatel uhodne pouze číslo, ale ne jeho umístění.

"""

import random
import time


def welcome_message():
    print("Hi there!")#program pozdraví užitele a vypíše úvodní text
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")

#vytvoří tajné 4místné číslo
def generate_secret_number():
    while True:
        secret_number = random.randint(1000, 9999)
        if len(set(str(secret_number))) == 4:
            return secret_number
            

def round_evaluation(secret_number, user_number):
    bulls = 0
    cows = 0
  
    number_find = (user_number.find(str(secret_number)[0]))
    if number_find == 0:
        bulls += 1
    elif number_find > -1:
        cows += 1
    number_find = (user_number.find(str(secret_number)[1]))
    if number_find == 1:
        bulls += 1
    elif number_find > -1:
        cows += 1
    number_find = (user_number.find(str(secret_number)[2]))
    if number_find == 2:
        bulls += 1
    elif number_find > -1:
        cows += 1
    number_find = (user_number.find(str(secret_number)[3]))
    if number_find == 3:
        bulls += 1
    elif number_find > -1:
        cows += 1

    return bulls, cows
        
    

def round_info (bulls, cows):
    bull_text = "bull"
    cow_text = "cow"
    if bulls > 1:
        bull_text = "bulls"

    if cows > 1:
        cow_text = "cows"

    print(f"{bulls} {bull_text}, {cows} {cow_text}\n{separator}")

def validate_guess (user_guess):
    return len(user_guess) != 4 or not user_guess.isdigit() or user_guess[0] == '0' or len(set(user_guess)) != 4

def game_results (atempts, time_start):
    time_stop = time.time()
    finish_time = time_stop - time_start
    seconds = finish_time / 60
    print("Your total time is", {seconds}, "seconds.")
    print("You've guessed the right number for", {atempts}, "atempts.")

def main():
    welcome_message()

    secret_number = generate_secret_number ()
    atempts = 0
    time_start = time.time()

    while True:
        user_guess = input("Enter a number ")
        atempts +=1
        if validate_guess (user_guess):
            print("Invalid input. Please enter 4 unique digits that don't start with 0.")
            continue
        bulls, cows = round_evaluation(secret_number, user_guess)
        round_info(bulls, cows)
        if bulls == 4:
            break

    game_results(atempts, time_start)

if __name__ == "__main__":
    main()