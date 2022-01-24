import random

print("Hangman in Python :-)")
erraten = []
woerter = 'Pause Ende Hallo'.split()
ratewort = random.choice(woerter)

print(ratewort)
for buchstaben in ratewort:
    print(" ", end='_')

    print("End")