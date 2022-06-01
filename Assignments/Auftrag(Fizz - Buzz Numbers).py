"""Auftrag - 011/07 (Fizz - Buzz Numbers)
izz Buzz ist eine berühmte Code-Herausforderung, die in Interviews verwendet wird, 
um grundlegende Programmierkenntnisse zu testen. 
Es ist an der Zeit, Ihre eigene Implementierung zu schreiben.
Drucken Sie Zahlen von 1 bis einschließlich 100, indem Sie diesen Anweisungen folgen:
wenn eine Zahl ein Vielfaches von 3 ist, drucke "Fizz" anstelle dieser Zahl,
wenn eine Zahl ein Vielfaches von 5 ist, drucke "Buzz" anstelle dieser Zahl,
für Zahlen, die Vielfache von 3 und 5 sind, geben Sie "FizzBuzz" aus,
geben Sie die restlichen Zahlen unverändert aus.
Geben Sie jeden Wert in einer separaten Zeile aus."""

for nummer in range(1,101):
    if nummer % 3 == 0 and nummer % 5 != 0:
        print("Fizz")
    elif nummer % 3 != 0 and nummer % 5 == 0:
        print("Buzz")
    elif nummer % 3 == 0 and nummer % 5 == 0:
        print("FizzBuzz")
    else:
        print(nummer)