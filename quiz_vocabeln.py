# Punkte
punkte = 0

# Weiter
def weiter():
    weiter = input("Bist du bereit für die nächste Frage?")
    if weiter.lower() == "ja":
        print("Super! Hier ist deine nächste Frage:")

# Korrekt
def korrekt():
    global punkte
    punkte += 1
    print("Korrekt! + 1 Punkt.")
    weiter()

# Falsch
def falsch():
    global punkte
    punkte -= 1
    print("Leider Falsch, das solltest du dir nochmal angucken... - 1 Punkt.")
    weiter()


# Anfangs Fragen
print("Herzlich Willkommen, ich bin deine Vokabel Hilfe.")
print("Dieses Programm soll dir beim Vokabeln lernen in Französisch helfen.")

thema = input("Zu welchem Thema möchtest du Vokabeln lernen (Essen oder Städte)?")


# Thema 1: Essen
if thema.lower() == "essen":

    print("Bonjour! Du hast dich für Vokabeln rund ums Thema Essen entschieden.")
    print("Ich werde dich nun in verschiedenen Weisen abfragen, bleib dran...")

    bereit = input("Bist du bereit?")
    if bereit.lower() == "ja":
        frage1 = input("Was ist das Verb für 'essen' auf französisch?")
        if frage1.lower() == "manger":
            korrekt()
        else:
            falsch()

        frage2 = input("Was bedeutet 'Milch' auf französisch?")
        if frage2.lower() == "lait":
            korrekt()
        else:
            falsch()

        frage3 = input("Ist 'Eau' eine Speise oder ein Getränk?")
        if frage3.lower() == "getränk":
            print("Richtig!")
            x = input("Und was ist es auf deutsch?")
            if x.lower() == "wasser":
                korrekt()
        else:
            falsch()

        frage4 = input("Wie sagt man 'das Frühstück' auf französisch (ohne Accents)?")
        if frage4.lower() == "le petit dejeuner":
            korrekt()
        else:
            falsch()

        frage5 = input("Was heißt 'der Apfel' auf französisch?")
        if frage5.lower() == "la pomme":
            korrekt()
        else:
            falsch()

        frage6 = input("Wie sagt man 'ich habe Hunger'?")
        if frage6.lower() == "j'ai faim":
            korrekt()
        else:
            falsch()

        frage7 = input("Was ist 'der Käse' auf französisch?")
        if frage7.lower() == "le fromage":
            korrekt()
        else:
            falsch()

        frage8 = input("Was ist 'le poisson' auf deutsch?")
        if frage8.lower() == "der fisch":
            korrekt()
        else:
            falsch()

# Ende + Punkte
        print("Fertig! Du hast" , punkte , "Punkte.")
        if punkte <=5:
            print("Du solltest das nochmal versuchen...")
    else:
        print("Dann halt nicht!")

# Thema 2: Städte
if thema.lower() == "städte":
    print("Bonjour! Du hast dich für Vokabeln rund ums Thema Städte entschieden")
    print("Ich werde dich nun in verschiedenen Weisen abfragen, bleib dran...")

    bereit = input("Bist du bereit?")
    if bereit.lower() == "ja":
        frage1 = input("Wie sagt man 'die Stadt'?")
        if frage1.lower() == "la ville":
            korrekt()
        else:
            falsch()

        frage2 = input("Was heißt 'die Hauptstadt'?")
        if frage2.lower() == "la capitale":
            korrekt()
        else:
            falsch()

        frage3 = input("Wie sagt man 'Ich lebe in Paris'? (ohne Accents)")
        if frage3.lower() == "j'habite a paris":
            korrekt()
        else:
            falsch()

        frage4 = input("Wie ist das Verb für 'wohnen' auf französisch?")
        if frage4.lower() == "habiter":
            korrekt()
        else:
            falsch()

        frage5 = input("Werden Städte auf französisch groß oder klein geschrieben?")
        if frage5.lower() == "groß":
            korrekt()
        else:
            falsch()

        frage6 = input("Wie sagt man 'die Altstadt' auf Französisch")
        if frage6.lower() == "la vieille ville":
            korrekt()
        else:
            falsch()

        frage7 = input("Was heißt 'die U-Bahn' auf Französisch (ohne Accents)?")
        if frage7.lower() == "le metro":
            korrekt()
        else:
            falsch()

        frage7 = input("Wie sagt man 'der Bahnhof' auf Französisch?")
        if frage7.lower() == "la gare":
            korrekt()
        else:
            falsch()
        
# Ende + Punkte
        print("Fertig! Du hast" , punkte , "Punkte.")
        if punkte <=5:
            print("Du solltest das nochmal versuchen...")
    else:
        print("Dann halt nicht!")
   