	
links = set("qwertasdfgyxcvb")

recht = set("zuiophjklmn")

wort = input("Geben sie ein Wort ein :")



wortneu = set(wort)

linker = bool(wortneu.intersection(links))

rechts = bool(wortneu.intersection(recht))

if (linker and rechts):

    print(wort , "ist bequeme worte!")

else:

    print(wort , "ist keine bequeme worte!")