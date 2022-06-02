giris="""
(1)topla
(2)cikar
(3)carp
(4)böl
(5)karesini hesapla
(6)kare kök hesapla
"""
print(giris)

soru=input("yapmak istediginiz islemin numarasini girin:")

if soru=="1":
    sayi1=int(input("Toplama islemi icin ilk sayiyi girin:"))
    sayi2=int(input("toplama islemi icin ikinci sayiyi girin"))
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)
elif soru=="2":
    sayi3=int(input("Cikarma islemi icin ilk sayiyi girin:"))
    sayi4=int(input("cikarma islemi icin ikinci sayiyi girin:"))
    print(sayi3,"-",sayi4,"=",sayi3-sayi4)
elif soru=="3":
    sayi5=int(input("carpma islemi icin ilk sayiyi girin:"))
    sayi6=int(input("carpma islemi icin ikinci sayiyi girin:"))
    print(sayi5,"*",sayi6,"=",sayi5+sayi6)
elif soru=="4":
    sayi7=int(input("bölme islemi icin ilk sayiyi girin:"))
    sayi8=int(input("bölme islemi icin ikinci sayiyi girin:"))
    print(sayi7,"/",sayi8,"=",sayi7+sayi8)
elif soru=="5":
    sayi9=int(input("karesini hesaplamak istediginiz sayiyi girin:"))
    print(sayi9,"sayinin karesi=",sayi9**2)
elif soru=="6":
    sayi10=int(input("kare kökünü hesaplamak istediginiy sayiyi girin:"))
    print(sayi10,"sayisinin karekökü=",sayi10**0.5)
else:
    print("Yanlis giris.")
    print("Asagidaki seceneklerden birini giriniz:",giris)
    
    
