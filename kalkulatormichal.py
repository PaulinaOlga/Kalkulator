liczbaA = 0
liczbaB = 0
operacja = " "


def dodaj(x, y):
    return x + y



def odejmij(x, y):
    return x - y



def pomnoz(x, y):
    return x * y



def podziel(x, y):
    return x / y


#wynik= input("Podaj działanie: (* / + -")  #tu jest string

liczbaA = int(input("Podaj liczbę A: "))
liczbaB = int(input("Podaj liczbę B: "))
operacja = input("Podaj działanie: (* / + -): ")  #potrzebujemy string


def wykonajDzialanie(operacja):
    if operacja =="*":
        return pomnoz (liczbaA, liczbaB)
    if operacja == "/":
        return podziel (liczbaA, liczbaB)
    if operacja =="+":
        return dodaj (liczbaA, liczbaB)
    if operacja == "-":
        return odejmij (liczbaA, liczbaB)

wynikDzialania = wykonajDzialanie(operacja)
print(wynikDzialania)



