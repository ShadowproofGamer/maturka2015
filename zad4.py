plik = open("liczby.txt")
dane = plik.read().split()
#print("dane: ", dane)

binarne_zera = []
for i in dane:
    zera = i.count('0')
    jedynki = i.count('1')
    #print(zera, " zer i ", jedynki, " jedynek")
    if zera>jedynki:
        binarne_zera.append(i)
print("ilośc liczb binarnych z większą ilością zer: ", len(binarne_zera))

podzielne_przez_2 = 0
podzielne_przez_8 = 0
integery = []
for j in dane:
    x = int(j, 2)
    integery.append(x)
    if x%2 == 0:
        podzielne_przez_2 += 1
    if x%8 == 0:
        podzielne_przez_8 += 1
print("podzielne przez 2: ", podzielne_przez_2, " i podzielne przez 8: ", podzielne_przez_8)
temp_max = temp_min = integery[0]

for k in integery:
    if k > temp_max:
        temp_max = k
    elif k < temp_min:
        temp_min = k
print("wiersz max: ", integery.index(temp_max), " i wiersz min: ", integery.index(temp_min))