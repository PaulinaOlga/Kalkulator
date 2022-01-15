# Napisz procedurę, która oblicza obwód trójkąta

w=int(input("Podaj 1 długość: "))
e=int(input("Podaj 2 długość: "))
r=int(input("Podaj 3 długość: "))




def policz_obwod(a,b,c):
    obwod = a + b + c
    #print(obwod) zamiast print:
    return (obwod)


obwod1 = policz_obwod(w,e,r)
print(obwod1)