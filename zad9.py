# Stosując pętle for przejdź przez listę liczb [1,2,3,4,5,6,25,24,65], jeśli liczba jest nieparzysta
# wypisz ją, w przeciwnym wypadku zastosuj continue

for i in [1, 2, 3, 4, 5, 6, 25, 24, 65]:
    if i % 2 == 0:
        continue
    else:
        print(i)
