# Punkte
punkte = 0

# Weiter
def weiter():
    weiter = input("Bist du bereit für die nächste Frage?")
    if weiter.lower() == "ja":
        print("Super! Hier ist deine nächste Frage:")

# Richtig
def richtig():
    global punkte
    punkte += 1
    print("Richtig! + 1 Punkt...")

# Falsch
def falsch():
    global punkte
    punkte -= 1
    print("Falsch! - 1 Punkt...")

# Quiz Start
print("Herzlich Willkommen beim Länder Quiz.")
print("Aber bevor es richtig los geht, musst du mir etwas wichtiges beantworten...")
x = input("Wie heißt der Programmierer dieses Quizzes?")
if x.lower() == "philipp":
    punkte += 1
    print("Du weißt Bescheid... + 1 Ehrenpunkt 💪")
elif x.lower() == "pika":
    punkte += 1
    print("Du weißt Bescheid... + 1 Ehrenpunkt 💪")
elif x.lower() == "pikachu":
    punkte += 1
    print("Du weißt Bescheid... + 1 Ehrenpunkt 💪")
else:
    punkte -= 1
    print("Wow, das ist hart peinlich...- 1 Punkt😣😂")

# Wie viele Fragen soll das Quiz beinhalten?
wie_viele = int(input("Möchtest du ein 3, 5 oder 10 Fragen Quiz?"))

# 3 Fragen Quiz
if wie_viele == 3:
    print("So, jetzt geht's los :) ")

    # Frage 1/3
    frage = input("In welchem Kontinent liegt die Türkei?")
    if frage.lower() == "europa":
        richtig()
    elif frage.lower() == "asien":
        richtig()
    else:
        falsch()

    # Frage 2/3
    frage = input("Für was steht die Abkürzung USA?")
    if frage.lower() == "vereinigte staaten von amerika":
        richtig()
    else:
        falsch()

    # Frage 3/3
    frage = input("Welches Land hat die größte Fläche der Welt?")
    if frage.lower() == "russland":
        richtig()
    else:
        falsch()

# 5 Fragen Quiz
elif wie_viele == 5:
    print("So, jetzt geht's los :) ")

    # Frage 1/5
    frage = input("In welchem Kontinent liegt die Türkei?")
    if frage.lower() == "europa":
        richtig()
    elif frage.lower() == "asien":
        richtig()
    else:
        falsch()

    # Frage 2/5
    frage = input("Für was steht die Abkürzung USA?")
    if frage.lower() == "vereinigte staaten von amerika":
        richtig()
    else:
        falsch()

    # Frage 3/5
    frage = input("Welches Land hat die größte Fläche der Welt?")
    if frage.lower() == "russland":
        richtig()
    else:
        falsch()

    # Frage 4/5
    frage = input("Welches Land hat am meisten Inseln?")
    if frage.lower() == "schweden":
        richtig()
    else:
        falsch()

    # Frage 5/5
    frage = input("Welches europäische Land hat keine Küste?")
    if frage.lower() == "schweiz":
        richtig()
    else:
        falsch()

# 10 Fragen Quiz
elif wie_viele == 10:
    print("So, jetzt geht's los :) ")

    # Frage 1/10
    frage = input("In welchem Kontinent liegt die Türkei?")
    if frage.lower() == "europa":
        richtig()
    elif frage.lower() == "asien":
        richtig()
    else:
        falsch()

    # Frage 2/10
    frage = input("Für was steht die Abkürzung USA?")
    if frage.lower() == "vereinigte staaten von amerika":
        richtig()
    else:
        falsch()

    # Frage 3/10
    frage = input("Welches Land hat die größte Fläche der Welt?")
    if frage.lower() == "russland":
        richtig()
    else:
        falsch()

    # Frage 4/10
    frage = input("Welches Land hat am meisten Inseln?")
    if frage.lower() == "schweden":
        richtig()
    else:
        falsch()

    # Frage 5/10
    frage = input("Welches europäische Land hat keine Küste?")
    if frage.lower() == "schweiz":
        richtig()
    else:
        falsch()

    # Frage 6/10
    frage = input("Was ist die Amtssprache in Brasilien?")
    if frage.lower() == "portugiesisch":
        richtig()
    else:
        falsch()

    # Frage 7/10
    frage = input("Welches Land ist bekannt für Pyramiden?")
    if frage.lower() == "ägypten":
        richtig()
    else:
        falsch()

    # Frage 8/10
    frage = input("In welchem Land liegt die Stadt Reykjavík?")
    if frage.lower() == "island":
        richtig()
    else:
        falsch()

    # Frage 9/10
    frage = input("Was ist die Hauptstadt von Kanada?")
    if frage.lower() == "ottawa":
        richtig()
    else:
        falsch()

    # Frage 10/10
    frage = input("Welches Land hat die längste Küstenlinie der Welt?")
    if frage.lower() == "kanada":
        richtig()
    else:
        falsch()

# Quiz Ende
print("Du hast" , punkte , "Punkte.")
