#Napisz program, który mając listę [1,2,3,4] pomnoży każy element listy dwukrotnie

lista = [1,2,3,4]
i = 0

while i < len(lista):
    #pobierz element i-ty z listy
    elementListy = lista[i]
    #pomnoz go razy 2
    pomnozonyElement = elementListy * 2
    #zapisz i-ty element listy
    lista[i] = pomnozonyElement

    print(lista[i])
    i = i + 1