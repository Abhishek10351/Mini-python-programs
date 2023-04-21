from random import choice
import datetime
from blessed import Terminal

term = Terminal()

a = list(range(1, 10))
b = list(range(10))
for i in range(4):
    if i == 0:
        try:
            j = choice(a)
            b.remove(j)
            key = j
        except ValueError:
            pass
    else:
        k = choice(b)
        b.remove(k)
        key = f"{key}{k}"
i = 0
score = 12
List = []
guesses = []

print("Enter h or help if you need help.")
info = """A random number will be generated from 1000 to 9999(called 'key').
Your job is to guess the number in 12 steps(You will get 12 prompts).
You will get help by the program.
It will show you the no of digits correctly placed and also digits which are in the key.
In the number genarated not a single digit will repeat.
After you enter a number it will be checked for errors.
If it is correct it will show you the previous numbers
If it is wrong the guess will not be counted
All the best for the game"""
print()
start = datetime.datetime.now()
while i != 12:
    #print(Terminal().clear())
    guess = input(f"Enter guess number {i+1}: ")
    win = False
    repeat = False
    if guess in "h help ?".split():
        print(info)
        continue
    if  not guess.isdigit():
        print('Can\'t accept a non numeric value')
        continue
    if guess in guesses:
        print("\nNumber already entered.")
        continue

    if len(guess) != 4:
        print("\nInvalid Value.\nPlease Enter a Integer From 1000 to 9999.")
        continue
    a = list(guess)
    for j in range(4):
        b = a.pop()
        if b in a:
            repeat = True
            break
    if repeat:
        print("\nNo Repetations Allowed")
        continue
    guesses.append(guess)
    print(Terminal().clear())
    if key == guess:
        win = True
        break
    else:
        position = 0
        for a in range(4):
            if key[a] == guess[a]:
                position = position + 1
        exist = 0
        for a in guess:
            if a in key:
                exist = exist + 1
        row = f"{guess}-> Correctly Entered: {position} , Exists: {exist}"
        List.append(row)
        print("\n")
        [ print(row) for row in List ]
        i = i + 1
        score = score - 1
stop = datetime.datetime.now() - start
if not win:
    print(f"You lost\nThe no was: {key} ")
elif win:
    message = f"""You Won.\nYour Score is: {score}.\nIt took you {i+1} steps.
    You completed it in {stop.seconds} seconds"""
    print(message)