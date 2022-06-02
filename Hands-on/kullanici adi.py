kullanici_adi=input("Kullanici Adiniz:")
parola=input("Parolaniz:")

toplam_uzunluk=len(kullanici_adi)+len(parola)

mesaj="Kullanici adi ve parolaniz toplam {} karakterden olusuyor!"

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk >40:
    print("kullanici adiniz ve parolanizin,"
          "toplam uzunlugu 40 karakteri gecmemeli!")

else:
    print("Sisteme Hosgeldiniz")
