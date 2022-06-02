anfang="""
(1)Addition
(2)Subtraktion
(3)Multiplikation
(4)Division
(5)Quadrat
(6)Quadratwurzel
"""

print(anfang)

schlüssel=1

while schlüssel==1:
    frage=input("Geben Sie die Nummer des Vorgangs ein,den Sie ausführen möchten(zum Beenden q):")
    if frage=="q":
        print("Verlassen des Programms")
        schlüssel==0
        
    elif frage=="1":
        zahl1=int(input("Geben Sie die erste Zahl für die Addition ein: "))
        zahl2=int(input("Geben Sie die zweite Zahl für die Addition ein: "))
        print(zahl1,"+",zahl2,"=",zahl1+zahl2)

    elif frage=="2":
        zahl3=int(input("Geben Sie die erste Zahl für die Subtraktion ein: "))
        zahl4=int(input("Geben Sie die zweite Zahl für die Subtraktion ein: "))
        print(zahl3,"-",zahl4,"=",zahl3-zahl4)

    elif frage=="3":
        zahl5=int(input("Geben Sie die erste Zahl für die Multiplikation ein: "))
        zahl6=int(input("Geben Sie die zweite Zahl für die Multiplikation  ein: "))
        print(zahl5,"*",zahl6,"=",zahl5*zahl6)

    elif frage=="4":
        zahl7=int(input("Geben Sie die erste Zahl für die Division ein: "))
        zahl8=int(input("Geben Sie die zweite Zahl für die Division ein: "))
        print(zahl7,"/",zahl8,"=",zahl7/zahl8)

    elif frage=="5":
        zahl9=int(input("Geben Sie die Zahl ein,für die Sie die Quadrat berechnen möchten: "))
        print("Das Quadrat von",zahl9,"ist: ",zahl9**2)

    elif frage=="6":
        zahl10=int(input("Geben Sie die Zahl ein,für die Sie die Quadratwurzel berechnen möchten: "))
        print("Das Quadratwurzel von",zahl10,"ist: ",zahl10**0.5)

    else:
        print("Falscher Eintrag.")
        print("Geben Sie eine der folgenden Optionen ein:",anfang)


