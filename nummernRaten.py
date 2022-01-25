import random

runde = 0
aktiv = True
computerzahl = random.randint(1,100)
#print(computerzahl)

while aktiv:
    runde = runde + 1
    print("Runde. " + str(runde))
    benutzereingabe = input("Bitte eine Zahl eingeben, zum beenden ende tippen: ")
    benutzereingabe = int(benutzereingabe)

    if benutzereingabe == computerzahl:
        print("gewonnen")
        aktiv = False
    elif benutzereingabe < computerzahl:
        print("Zahl ist zu klein")
    else:
        benutzereingabe > computerzahl
        print("Zahl ist zu groß")
    
    if runde == 7:
        print("Leider verloren")
        print("die gesuchte Zahl war: " + str(computerzahl))
        aktiv = False
    if benutzereingabe == "ende":
        aktiv = False
print("und tschüss")