#a = 0
#b = 100

#while a <= 100:
    #a = a + 5
    #if a > 100:
        #break
    #if a == 50:
        #a += 10
        #continue
   # print(a, end= ' ')

x = int(input("Podaj liczbę mieszkańców: "))
i = 0    #ilość wejść do pętli
suma = 0

while i < x:
    i+= 1
    y = int(input("Podaj wiek domownika " + str(i) + ": "))
    suma = y + suma

print ("Średnia wieku domowników: " + str(suma/x))



