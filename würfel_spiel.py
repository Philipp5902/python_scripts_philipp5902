from random import randint

punkte_spieler = 0
punkte_computer = 0

print("🎲 Der mit der höheren Zahl erhält 1 Punkt. Wer zuerst 5 Punkte hat, gewinnt!")

while True:
    start = input("Möchtest du würfeln oder beenden? ").strip().lower()

    if start == "beenden":
        print("Spiel beendet")
        break
    elif start == "würfeln":
        computer = randint(1, 6)
        wurf = randint(1, 6)

        print("Du würfelst:", wurf)
        print("Ich würfle:", computer)

        if wurf == computer:
            print("Gleichstand!")
        elif wurf > computer:
            punkte_spieler += 1
            print("1 Punkt für dich!")
        else:
            punkte_computer += 1
            print("1 Punkt für mich!")
        print(f"Du: {punkte_spieler} | Ich: {punkte_computer}")

        if punkte_spieler == 5:
            print("🎉 Glückwunsch, du hast gewonnen!")
            break
        elif punkte_computer == 5:
            print("😎 Haha, ich habe gewonnen, vielleicht klappt's beim nächsten Mal...")
            break
    else:
        print("Bitte gib 'würfeln' oder 'beenden' ein.")
