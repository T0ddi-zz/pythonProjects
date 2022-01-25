import random

print("Hangman in Python :-)")

# Speichern von erratenen Buchstaben
erraten = []

# Eingabe Benutzer
benutzereingabe = ""

# Woerterliste
woerter = 'Hund Katze Maus Fliege Vogel Giraffe Freddie'.split()
ratewort = random.choice(woerter)
# Ratewort ausgeben
# print(ratewort)

# Buchstaben in Wort ersetzen
for buchstaben in ratewort:
    #print(" ", end='_')
    erraten.append('_')

while benutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=' ')
    print() # fuer nächste Zeile
    benutzereingabe = input("Dein erster Buchstabe: ")
    x = 0
    
    # Ueberpruefung, ob Buchstaben in Wort
    for buchstaben in ratewort:
        if buchstaben.lower() == benutzereingabe.lower():
            # print("richtig")
            erraten[x] = buchstaben
        x += 1
    print()

    # Gewonnen?
    if '_' in erraten:
        print("noch nicht gewonnen")
    else:
        print("Gewonnen")
        break