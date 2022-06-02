kullanici_adi=input("Kullanici Adiniz:")
parolaniz=input("Parolaniz:")

toplam_uzunluk=len(kullanici_adi)+len(parolaniz)

mesaj="kullanici adi ve porolaniz {}toplam karakterden olusuyor!"

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk > 40:
      print("Kullanici adiniz ve parolanizin",
            "toplam uzunlugu 40 karakteri gecmemeli!")
else:
    print("Sisteme Hosgeldiniz")
