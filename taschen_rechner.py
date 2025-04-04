print("Hallo! Ich bin deine Rechenhilfe!")
print("Wähle dazu einfach zwischen verschiedenen Befehlen aus:")
print("Addition, Subtraktion, Multiplikation, Division und beenden.")

while True:
    auswahl = input("Was möchtest du machen?")

    if auswahl == "Addition":
        try:
            zahl1 = float(input("Wie lautet deine erste Zahl?"))
            zahl2 = float(input("Wie lautet deine zweite Zahl?"))
            print("Dein Ergebnis ist:", zahl1 + zahl2)

        except ValueError:
            print("Ungültige Eingabe!")

    elif auswahl == "Subtraktion":
        try:
            zahl1 = float(input("Wie lautet deine erste Zahl?"))
            zahl2 = float(input("Wie lautet deine zweite Zahl?"))
            print("Dein Ergebnis ist:", zahl1 - zahl2)

        except ValueError:
            print("Ungültige Eingabe!")

    elif auswahl == "Multiplikation":
        try:
            zahl1 = float(input("Wie lautet deine erste Zahl?"))
            zahl2 = float(input("Wie lautet deine zweite Zahl?"))
            print("Dein Ergebnis ist:", zahl1 * zahl2)

        except ValueError:
            print("Ungültige Eingabe!")

    elif auswahl == "Division":
        try:
            zahl1 = float(input("Wie lautet deine erste Zahl?"))
            zahl2 = float(input("Wie lautet deine zweite Zahl?"))
            print("Dein Ergebnis ist:", zahl1 / zahl2)

        except ValueError:
            print("Ungültige Eingabe!")

    elif auswahl == "beenden":
        try:
            print("Bis bald!")
            break

        except ValueError:
            print("Ungültige Eingabe!")

    else:
        print("Ungültige Eingabe! Bitte wähle eine der angegebenen Befehle!")