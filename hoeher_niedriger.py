from random import randint

# Start
print("Ich gebe dir eine Karte. Du musst entscheiden, ob meine zweite Karte höher oder niedriger als die erste ist")
print("Wenn du richtig liegst, bekommst du einen Punkt.")
print("Es gibt nur Karten 1- 10.")

# Spiel
while True:
    # Karten
    karte_1 = randint(1, 10)
    karte_2 = randint(1, 10)
    try:
        start = input("Willst du die erste Karte sehen?")
        if start.lower() == "ja":
            print("Deine erste Karte:", karte_1)
            print("Okay, ich habe die zweite Karte gezogen.")rb
            weiter = input("Denkst du sie ist höher oder niedriger als die erste?")
            weiter_2 = input("Hallo, möchtest du fortfahren? Wenn nicht,")
            if weiter.lower() == "höher":
                if karte_2 >= karte_1:
                    print("Deine zweite Karte:", karte_2)
                    print("Richtig!")
                else:
                    print("Leider falsch")
            if weiter.lower() == "niedriger":
                if karte_2 <= karte_1:
                    print("Deine zweite Karte:", karte_2)
                    print("Richtig!")
                else:
                    print("Leider falsch")
            elif start.lower() == "nein":
                print("Programm beendet.")

            if karte_1 == karte_2:
                print("Die Karten sind gleich groß.")
                
    except ValueError:
        print("Ups, hier gab es einen Fehler. Programm beendet.")
        break
    
        except IndexError:
        print("Ups, hier gab es einen Fehler. Programm beendet.")
        break