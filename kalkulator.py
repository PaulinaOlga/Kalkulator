liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
znak = input("Podaj znak działania: (* / + -): ")
print("wynik równa się: ")

if znak == "+":
    print( str(liczba1 + liczba2))
elif znak == "-":
    print( str(liczba1 - liczba2))
elif znak == "/":
    print( str(liczba1 / liczba2))
elif znak == "*":
    print(str(liczba1 * liczba2))
elif znak == "**" or znak == "^":
    print(str(liczba1 ** liczba2))
elif znak == "%":
    print(str(liczba1 % liczba2))
elif znak == "p":
    print(liczba1*liczba2 * 0.01)