#Napisz program, który mając listę [1,2,3,4] pomnoży każdy element listy dwukrotnie
#i zapisze w nowej, osobnej liście

import qrcode
img = qrcode.make("http://www.google.pl")
img.save("qrcode.jpg")

lista = [1,2,3,4]
listaA = []

for x in lista:
    mnozenie = x * 2
    listaA.append(mnozenie)  #dodaj element do listy

print(listaA)


