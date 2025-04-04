einkaufsliste = []

print("Hey, ich bin deine Einkaufslisten-Hilfe!")

while True:
    entscheidung = input(
        "Möchtest du einen Artikel hinzufügen, entfernen, beenden oder die Liste anzeigen (hinzufügen / entfernen / anzeigen / beenden)?")
    if entscheidung == "hinzufügen":
        item = input("Was möchtest du hinzufügen?")
        einkaufsliste.append(item)
        print(item , " wurde zu deiner Einkaufsliste hinzugefügt")

    if entscheidung == "entfernen":
        delete = input("Was möchtest du entfernen?")
        einkaufsliste.remove(delete)
        print(delete , " wurde entfernt")

    if entscheidung == "anzeigen":
        print(einkaufsliste)

    if entscheidung == "beenden":
        print("Bis bald!")
        break

    else:
        print("Ungültige Eingabe! Bitte gib 'hinzufügen', 'entfernen', 'anzeigen' oder 'beenden' ein.")