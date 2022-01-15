# Napisz program, który mając listę {1,2,3,4,5,6] wypisze pierwsze trzy elementy listy, a następnie
# usunie je z listy.

# Rozwiązanie pętlą for
#lista1 = [1,2,3,4,5,6]

#lista1 = [e for i,e in enumerate(lista1) if i >= 3]
#print(lista1)

lista1 = [1,2,3,4,5,6]

for i in lista1:
    if i <= 3:
        print(i)

print(lista1[0:3])

x = 1
while x <= 3:
    lista1.remove(x)
    x = x + 1

print(lista1)

