n = int(input("Welche Zahl willst du testen? "))

p = 1
prim = True
if n == 1:
    prim = False
else:
    i = 2
    while i <= n - 1:
        if n % i == 0:
            prim = False
        i += 1
if prim:
    print(n, "ist eine Primzahl.")
else: print(n, "ist keine Primzahl.")