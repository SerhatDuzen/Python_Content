#Tamsayiyi ondalik sayiya cevirme

a = 49
a = float(a)
print(a) # 49.0 output
print(float(37)) # 37.0 output

#Ondalik sayiyi tam sayiya cevirme

b = 2.98
b=int(b)
print(b) #int e cevirmede kucuk sayiya yuvarlar(Negatiflerde de buyuk olan)

#Sayiyi stringe cevirme / her rakam string karakteri olur

c = 346
c = str(c)
print(c)
d = str(9.432)
print(d)

#Stringi int e ya da float a cevirmek

a = "12345678h"
#a = int(a) hata verir cunku stringin icersinde sayi disinda bir karakter bulunmakta
b = '12387653241'
b = int(b)
print(b)
c = '56.654453'
c = float(c)
print(c) #56.654453 ciktisini verir

