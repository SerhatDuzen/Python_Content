#belirli bir kosulun olusmasina gore calisan kod bloklaridir

# if ilk kosul durumunu anlatir. eger bu kosul gerceklesmezse
#alttaki satira gecilir. elif ile diger kosul durumlari test edilir
#hicbir kosul olmaz ise else komutu calisir
#else opsiyoneldir. else olmadiginda ve hicbi kosul durumu true olmadiginda
#hicbir kod calismayacaktir


notortalamasi = int(input("Lutfen notunuzu giriniz: "))
if notortalamasi >= 90:
    print("AA")
elif notortalamasi >= 85:
    print("BA")
elif notortalamasi >= 90:
    print("BA")
elif notortalamasi >= 80:
    print("BB")
elif notortalamasi >= 75:
    print("CB")
elif notortalamasi >= 70:
    print("CC")
elif notortalamasi >= 65:
    print("DC")
elif notortalamasi >= 60:
    print("DD")
else:
    print("Dersten Kaldınız")