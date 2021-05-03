
#listelere benzer ancak tuple degistirilemez

myTuple = (1,2,3,4,5,9,8,7,6,5,1,2,5,1)
print(myTuple[3])
print(myTuple[2:])

#sadece 2 methodu vardir count ile degerin kac defa gectigini doner

print(myTuple.count(1)) #1 degeri 3 kez gecmistir

demet2 = ("Istanbul","Ankara","Izmir")
print(demet2.index("Izmir"))
#print(demet2.index("Van")) olmayan deger hata cikarir

#read only liste tipidir 123