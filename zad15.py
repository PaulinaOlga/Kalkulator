# Używając pętli while napisać kod, który poprosi o wypisanie trzech wartości.
# Po wypisaniu tych wartości mają być one podsumowane

a = 1
suma = 0
while a < 4:
    print("Podaj liczbę nr " + str( a))
    b = int(input())
    suma = suma + b
    a += 1
print("suma liczb wynosi: ", suma)

