
#Liste olusturma : listede farkli degiskenler bir arada bulundurulabilir

liste = ["Elma",87,5.22,"Ankara"]
print(type(liste))
liste2 = [] #bos liste olusturma
liste3 = list() #bos liste olusturma

#liste uzunlugunu bulma
print(len(liste))

#stringi listeye cevirme
liste4= list("Merhaba uzaylilar")
print(liste4)

#listeleri indexleme ve parcalama (Stringler ile benzer)
liste5 = [1,2,3,4,5,6,7,"Ankara","Trabzon"]
print(liste5[7])
print(liste5[2:])
print(liste5[:3])
print(liste5[::-1])

#liste islemleri

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1+liste2
print(liste3)

print(liste2*3)

#liste elemanlari dogrudan degistirlilebilirler

liste = [7,8,9,6,5,4]
liste[2]=99
print(liste)

#ilk 2 elemani degistirme

liste[:2] = [77,55]

#append methodu - verilen deger listeye eklenir

liste.append(876)

#pop methodu / son elemanini siler / attigi degeri dondurur

print(liste.pop())

#sort methodu 

liste = [1,6,4,2,9,5,66]
liste.sort()
print(liste)
liste.sort(reverse=True) #tersten siralar

#olmayan range verilirse hata
#liste[50]

#inner list

liste = [[1,2],['a','b'],[4,9]]

print(liste[1][1]) # b degerine ulasiriz





