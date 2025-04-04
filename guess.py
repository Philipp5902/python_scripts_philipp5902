from random import randint
zahl = randint(1, 100)

zeit = 0

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht :)")
print("Denkst du, du kannst sie mit weniger als 10 Versuchen erraten?")

while True:
    versuch = int(input("Rate meine Zahl: "))
    zeit = zeit + 1

    if versuch == zahl:
        print("Super, du hast die Zahl erraten!")
        print("Du hast so viele Versuche gebraucht:", zeit)
        break

    elif versuch <=zahl:
        print("Deine Zahl ist zu klein!")


    elif versuch >=zahl:
        print("Deine Zahl ist zu hoch")

    else:
        print("Ups, hier gab es einen Fehler! Bitte versuche es erneut!")