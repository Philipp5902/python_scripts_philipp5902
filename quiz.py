print("Hallo! Ich bin Quizzie.")
print("Ich habe mir 5 Fragen für dich ausgedacht.")
print("Pro richtiger Frage bekommst du 1 Punkt.")
print("Wenn du falsch antwortest, verlierst du einen Punkt.")

punkte = 0  # Punktestand initialisieren

anfang = input("Bist du bereit?")

if anfang.lower() == "ja":
    # Frage 1
    print("Frage 1:")
    frage1 = input("Was ist die Hauptstadt von Belgien? ")

    if frage1.lower() == "brüssel":
        punkte += 1  # Punktestand erhöhen
        print("Richtig! Du hast", punkte, "Punkt/e.")
    else:
        punkte -= 1  # Punktestand verringern
        print("Geo ist wohl nicht dein stärkstes Fach... du hast", punkte, "Punkt/e.")

    # Frage 2
    weiter1 = input("Möchtest du weitermachen?")
    if weiter1.lower() == "ja":
        print("Frage 2:")
        frage2 = input("Was ist die größte Stadt der Welt? ")

        if frage2.lower() == "tokyo":
            punkte += 1
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e.")

    # Frage 3
    weiter2 = input("Möchtest du weitermachen?")
    if weiter2.lower() == "ja":
        print("Frage 3:")
        frage3 = input("Welches Element hat das chemische Symbol 'O'?")
        if frage3.lower() == "sauerstoff":
            punkte += 1
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e.")

    # Frage 4
    weiter3 = input("Möchtest du weitermachen?")
    if weiter3.lower() == "ja":
        print("Frage 4:")
        frage4 = input("Wie viele Beine hat ein Insekt?")
        if frage4 == "6":
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e.")

    # Frage 5
    weiter4 = input("Möchtest du weitermachen?")
    if weiter4.lower() == "ja":
        print("Frage 5:")
        frage5 = input("Was ist das größte Tier der Welt?")
        if frage5.lower() == "blauwal":
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e.")

    # Ende
    print("Du hast" , punkte , "Punkte!")
    if punkte <= 2:
        print("Beim nächsten mal klappts vielleicht besser...")