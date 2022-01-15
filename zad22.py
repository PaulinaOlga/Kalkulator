# Napisz program, który poprosi o wypisanie wieku mamy i taty.
# Następnie napisz funkcję, która obliczy różnicę ich wieku i zwróci jej wartość

wiekm = int(input("Podaj wiek mamy: "))
wiekt = int(input("Podaj wiek taty: "))

def roznica_wieku (m, t):
    if m<t:
        roz= t - m
    elif t<m:             #lub else: roz= m - t
        roz= m - t
    return roz


wynik= roznica_wieku(wiekm, wiekt)
print(wynik)

#

