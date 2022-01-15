# Chcemy kupić książkę, ale obecna cena wynosi 60, a my chcemy kupić ją za 30.
# Stwórz pętle obniżającą cenę książki do momentu, w którym ją kupimy

cena = 60

while True:
    cena = cena -1
    print(cena)
    if cena == 30:
        break
print("Kupione")