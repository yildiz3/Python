#her ayin kac gün cektigini tanimliyoruz
ocak=mart=mayis=temmuz=agustos=ekim=aralik=31
nisan=haziran=eylül=kasim=30
subat=28

#dogalgazin vergiler dahil metreküp fiyati
birimfiyat=0.79

#kullanici ayda ne kadar dogalgaz tüketmis?
ayliksarfiyat=input("aylik dogalgaz fiyatinizi metreküp olarak giriniz:")


#kullanici hangi aya ait dogalgaz faturasini ögrenmek istiyor
dönem=input("""Hangi aya ait faturayi hesaplamak istersiniz?
(Lütfen ay adini tamami kücükharf olacak sekilde giriniz)\n""")

#Yukarıdaki input() fonksiyonundan gelen veriyi
#Python'ın anlayabileceği bir biçime dönüştürüyoruz
ay=eval(dönem)

#kullanicinin günlük dogalgaz sarfiyati.
günlüksarfiyat=int(ayliksarfiyat)/ay

#fatura tutari
fatura=birimfiyat*günlüksarfiyat*ay

print("günlük sarfiyatiniz:\t",günlüksarfiyat,"metreküp\n",
      "tahmini fatura tutari:\t",fatura,"TL",sep="")
