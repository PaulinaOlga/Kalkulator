x = int(input("Podaj liczbę dorosłych przy stoliku: "))
z = int(input("Podaj liczbę dzieci przy stoliku: "))


def rachunek(l_dorosli, l_dzieci):

    if l_dorosli %2 != 0:
        l_dorosli = l_dorosli + 1

    if l_dzieci %2 != 0:
        l_dzieci = l_dzieci + 1

    rach = (l_dorosli/2) * 30 + (l_dzieci/2) * 20

    print(rach)

rachunek(x, z)