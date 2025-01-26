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

# separator
separator = 70 * "-"

#program pozdraví užitele a vypíše úvodní text
print("Hi there!")

# separator
print(separator)

print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")

# separator
print(separator)

#vytvoří tajné 4místné číslo
while True:
    secret_number = random.randint(1000, 9999)
    if len(set(str(secret_number))) == 4:
        break
  
time_start = time.time()
user_number = 0

while user_number!= secret_number:
    user_number = input("Enter a number")
    bulls = 0
    cows = 0
    if len(user_number) !=4 :#nesmí zadt číslo kratší nebo delší než 4 čísla
        print("The number must have 4 digitis")
        continue
    if not user_number.isnumeric():#nesmí obsahovat nečíselné znaky
        print("Pleas put the number")
        continue
    if user_number.startswith ("0"):#nesmí začínat 0
        print("Sorry, the number not start whit 0")
        continue
    if len(set(user_number)) != 4:#nesmí obsahovat duplicity
        print("Input contains duplicate digits.")
        continue

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

time_stop = time.time()
finish_time = time_stop - time_start
seconds = finish_time / 60
print("Your total time is", {seconds}, "seconds.")

