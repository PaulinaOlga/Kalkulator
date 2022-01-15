# Napisz program, który zwróci informację czy liczba jest parzysta czy nie

czyliczba_parzy= int(input("Podaj liczbę: "))

wynik= czyliczba_parzy % 2

if wynik == 0:                              #def czyLiczbaParzysta(liczbax)
    print("Liczba jest parzysta")           #   return
else:
    print("liczba jest nieparzysta")


