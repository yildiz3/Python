nummer = input("Bitte geben Sie eine Ganzzahl ein: ")
ergebnis = 0
if nummer.startswith("-") or "." in nummer or "," in nummer or (not nummer.isdigit()):
    print("Es ist ein ungültiger Eintrag.Verwenden Sie keine nicht numerischen, Float- oder negativen Werte!")
else:
    for i in nummer:
        ergebnis = ergebnis + int(i) ** len(nummer)
    if int(nummer) == ergebnis:
        print(nummer, "ist eine Armstrong-Zahl")
    else:
        print(nummer, "ist keine Armstrong-Zahl")
        