#print fonksiyonu ekrana yazi yazdirmak icin kullanilir
print(36)
print(23.65)
print('Python programlama dili')
a=4
b=6
print(a+b)

#print fonksiyonunda birden fazla deger yazdirmak istersek bunlari virgul ile ayiririrz
print(a,"Ankara",b,88.5) # aralarinda auto olarak bir space vererek yazdirir

# \n imleci alt satira \t ise imleci bir tab ilerletir
print("Ankara\nIstanbul\tIzmir")

#type fonksiyonu aldigi parametrenin hangi tipte oldugunu dondurur
type("Murat") #str dondurur
type(321) #int dondurur
r = type(54.3)
print(r) #<class 'float'> yazdirir

#sep parametresi yazdirirken araya birakilmak istenen bosluk karakterleri
print(21,65,32,90,sep='/') #21/65/32/90 output
print("Ankara","Istanbul","Izmir",sep="\n")

#* li parametre her karakterin arasina bosluk koyar
print(*"JavaPythonc#") #J a v a P y t h o n c #
print(*"JavaPythonc#",sep='_') #J_a_v_a_P_y_t_h_o_n_c_#

#formatlama
a = 43
b = 87
print("{} ile {} nin toplami {} dir.".format(a,b,a+b)) #43 ile 87 nin toplami 130 dir.
#suslu parantezlere formatta verilen parametrelerin indexleri yazilabilir
print("{1} adli ogrencinin vize notu {2} dir\nFinal notu {0} dir".format(b,"Ali",a))




