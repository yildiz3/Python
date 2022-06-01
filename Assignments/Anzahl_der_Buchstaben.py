"""Aufgabe:

Zähle die Anzahl jedes Buchstabens in einem Satz.
Die Abteilung, für die Sie arbeiten, hat eine Projektkonstruktion durchgeführt, die eine Wort- / Textanalyse durchführt. 
Sie werden gebeten, die Anzahl der Buchstaben oder Zeichen in den unter diesem Projekt eingegebenen Sätzen zu berechnen.
Schreiben Sie ein Python-Programm, das;
nimmt einen Satz vom Benutzer,
zählt die Anzahl jedes Buchstabens/Zeichens des Satzes,
sammelt die Buchstaben/Zeichen als Schlüssel und die gezählten Zahlen als Wert in einem Wörterbuch .

satz = input("Bitte geben Sie einen Satz ein:  ")
mein_dict = {}
for buchstabe in satz:
    if buchstabe not in mein_dict:
        mein_dict[buchstabe] = 1
    else:
        mein_dict[buchstabe] += 1
print(mein_dict)