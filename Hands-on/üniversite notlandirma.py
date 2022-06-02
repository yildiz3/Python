x = int(input("Notunuz: "))
if x > 100 or x < 0:
    print("Böyle bir not yok")
elif x >= 90 and x <= 100:
    print("A aldınız.")
elif x >= 80 and x <= 89:
    print("B aldınız.")
elif x >= 70 and x <= 79:
    print("C aldınız.")
elif x >= 60 and x <= 69:
    print("D aldınız.")
elif x >= 0 and x <= 59:
    print("F aldınız.")

