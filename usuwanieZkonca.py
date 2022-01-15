# Napisz program, który mając listę [1,2,3,4,5,6] wypisze ostatnie trzy elementy listy,
# a następnie usunie je z listy.

lista = [1,2,3,4,5,6]

print(lista[-3:])
x = 0

max = len(lista)
while x < max:
    if max - x >=4:
        lista.pop()
    x = x + 1

print(lista)
