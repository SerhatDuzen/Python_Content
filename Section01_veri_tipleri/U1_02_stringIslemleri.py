str = "Python programlama dili cok pratik bir dil"

print(str[3:15:2])

print(str[3:])

print(str[:12])

#2 ser atlayarak yazdir

print(str[::2])

#stringi tersten yazdir

print(str[::-1])

#len int olarak stringin uzunlugunu dondurur

print(len(str))

#3 adet string tanimlayarak onlari ardarda yazdiralim

a = "Edirne "
b= "Tekirdag ve "
c = "Kirklareli "

print(a+b+c+"trakyada bulunan illerdir.")

#stringi birden fazla defa yazdirma

print(b*7)

#stringin karakterleri degistirilemez  - ancak string = assignment ile yeniden yazilip degisik
#bir deger verilebilir

i = "Serhat"
# i[3]=k HATA VERECEKTIR

i = i + " Python Developer"

print(i)  # Serhat Python Developer yazdirir


