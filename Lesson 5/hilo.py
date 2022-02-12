# Exercise 5 from aula05

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)
    print("Can you guess my secret?")

    tentative = 1
    chosen = int(input("What's your choice? "))

    while secret != chosen:
        if chosen < secret:
            print("Your number is lower.")
        
        elif chosen > secret:
            print("Your number is higher.")
        
        tentative += 1
        chosen = int(input("What's your choice? "))

    print(f"You're right! {secret} was the right number. You took {tentative} times to guess the number.")

main()
