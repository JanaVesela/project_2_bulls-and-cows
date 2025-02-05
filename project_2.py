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
    """
    program pozdraví užitele a vypíše úvodní text
    """
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")

#vytvoří tajné 4místné číslo
def generate_secret_number():
    """
    program vytvoří tajné 4místné číslo
    """
    while True:
        secret_number = random.randint(1000, 9999)
        if len(set(str(secret_number))) == 4:
            return secret_number
            

def round_evaluation(secret_number, user_number):
    bulls = 0
    cows = 0
    for x in range(4):
        number_find = (user_number.find(str(secret_number)[x]))
        if number_find == x:
            bulls += 1
        elif number_find > -1:
            cows += 1
    
    return bulls, cows

def round_info (bulls, cows):
    """   
    vypisuje spravně uhodnutá čísla, v množném a jednotném čísle
    """
    bull_text = "bull"
    cow_text = "cow"
    if bulls > 1:
        bull_text = "bulls"

    if cows > 1:
        cow_text = "cows"

    print(f"{bulls} {bull_text}, {cows} {cow_text}")

def validate_guess (user_guess):
    """
    číslo zadané uživatelem, nesmí být kratší nebo delší než 4 čísla,
    nesmí obsahovat duplicity, nesmí začínat nulou, nesmí obsahovat nečíselné znaky    
    """
    return len(user_guess) != 4 or not user_guess.isdigit() or user_guess[0] == '0' or len(set(user_guess)) != 4

def game_results (atempts, time_start):
    """
   vypisuje čas ve hře v sekundách a počet pokusů
    """
    time_stop = time.time()
    finish_time = time_stop - time_start
    seconds = finish_time / 60
    print(f"Your total time is {seconds} seconds.")
    print(f"You've guessed the right number for {atempts} atempts.")

def main():
    """
    zde uživatel hádá čtyřciferná čísla a podle úspěšnosti (uhádnutí správné
    číslice nebo její pozice) dostává zpětnou vazbu ve formě bodového ohodnocení. 
    "bulls" (býci), pokud uživatel uhodne jak číslo, tak jeho umístění 
    "cows" (krávy), pokud uživatel uhodne pouze číslo, ale ne jeho umístění

    spustí se počítání času a počítání pokusů

    když uživatel číslo uhodne ukáží se mu výsledky
    """
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