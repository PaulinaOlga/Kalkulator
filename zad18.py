# Używając pętli for napisz kod, który poprosi o wypisanie trzech wartości.
# Po wpisaniu tych wartości mają być one zsumowane.

suma = 0
for a in range (1,4):
        print("Podaj liczbę nr " + str(a))
        b = int(input())
        suma = suma + b
print("suma liczb wynosi: ", suma)