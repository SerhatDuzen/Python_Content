liste = [1,2,3,4,5,6,7,8,4,5,6,3,2,1,2,3,4,5]

# for bir liste, tuple, string gibi verilerin icerisinde dolasmamizi saglayan dongudur

a = 1
for i in liste:
    print("Listenin {}'inci elemani = {}'dir.".format(a,i))
    a+=1
    
    
sehir = "istanbul"

for ch in sehir:
    print(" ** ",ch," ** ")
    
    
liste2 = [{5,6}, {7,3}, {9,2}]

for (i,j) in liste2:
    print(i*j)