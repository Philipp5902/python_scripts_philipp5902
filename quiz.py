def gib_tipp():
    tipp = input("Brauchst du einen Tipp?")
    if tipp.lower() == "ja":
        welcher_tipp = int(input("Für welche Frage?"))
    # Tipp 1
        if welcher_tipp == 1:
            print("Anfangsbuchstabe ist ein B...")
    # Tipp 2
        if welcher_tipp == 2:
            print("Liegt in Japan...")
    # Tipp 3
        if welcher_tipp == 3:
            print("Wir atmen es ein...")

    # Tipp 4
        if welcher_tipp == 4:
            print("Eine Spinne hat 8 Beine und ist kein Insekt...")

    # Tipp 5
        if welcher_tipp == 5:
            print("Dieses Tier lebt im Wasser und ist wirklich riesig...")

print("Hallo! Ich bin Quizzie.")
print("Ich habe mir 5 Fragen für dich ausgedacht.")
print("Pro richtiger Frage bekommst du 1 Punkt.")
print("Wenn du falsch antwortest, verlierst du einen Punkt.")

punkte = 0  # Punktestand

anfang = input("Bist du bereit?")

if anfang.lower() == "ja":

    # Frage 1
    print("Frage 1:")
    print("Was ist die Hauptstadt von Belgien? ")
    gib_tipp()
    frage1 = input("Antwort:")
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
        print("Was ist die größte Stadt der Welt? ")
        gib_tipp()
        frage2 = input("Antwort:")
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
        print("Welches Element hat das chemische Symbol 'O'?")
        gib_tipp()
        frage3 = input("Antwort:")
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
        print("Wie viele Beine hat ein Insekt?")
        gib_tipp()
        frage4 = input("Antwort:")
        if frage4 == "6":
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e.")

    # Frage 5
    weiter4 = input("Möchtest du weitermachen?")
    if weiter4.lower() == "ja":
        print("Frage 5:")
        print("Was ist das größte Tier der Welt?")
        gib_tipp()
        frage5 = input("Antwort:")
        if frage5.lower() == "blauwal":
            print("Richtig! Du hast", punkte, "Punkt/e.")
        else:
            punkte -= 1
            print("Das war wohl nix... du hast", punkte, "Punkt/e")

    # Ende
    print("Du hast" , punkte , "Punkte!")
    if punkte <= 2:
        print("Beim nächsten mal klappts vielleicht besser...")