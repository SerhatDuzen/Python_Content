
#belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder.
# while döngüleri true oldugu surece evam eder sart bozulursa sonlanir

i=10
while i>0:
    print('pyhton')
    i-=1
    #10 defa python yazdirir
    
    
#while true kullanimi ile dongu icinde break komutu le sonlandirilmadikca dongu devam eder
sayac=3
while True:
    sifre=int(input("Lutfen sifreyi giriniz : "))
    if sifre == 123:
        print("giris islemi basarili")
        break
    sayac -=1
    if sayac == 0:
        print("3 kez yanlis sifre girdiginiz icin hesabiniz bloke edildi!!!")
        break
    print("Yanlis sifre tekrar deneyiniz")
    