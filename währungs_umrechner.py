print("Wähle zwischen Dollar, Pfund, Japanischer Yen,")
print("Schweizer Franken, Australische Dollar, Kanadische Dollar und Chinesische Yuan!")

while True:
    question = input("In welche Währung willst du Euro umrechnen? Wenn du aufhören möchtest, tippe beenden.")
    if question == "Dollar":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 1.08 , "Dollar")

    elif question == "Pfund":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 0.84 , "Pfund")

    elif question == "Japanischer Yen":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 162.24 , "Yen")

    elif question == "Schweizer Franken":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 0.98 , "Schweizer Franken")

    elif question == "Australische Dollar":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 1.63 , "Australische Dollar")

    elif question == "Kanadische Dollar":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 1.47 , "Kanadische Dollar")

    elif question == "Chinesische Yuan":
        x = float(input("Wie viel Euro hast du?"))
        print("Das wären" , x * 7.85 , "Chinesische Yuan")

    elif question == "beenden":
        print("Bis bald!")
        break

    else:
        print("Ungültige Eingabe! Bitte nutze die angegebenen Befehle!")