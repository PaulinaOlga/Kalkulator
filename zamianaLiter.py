#Napisz program, który zamieni czwartą literę w napisie "Racecar" na literę Z
#oraz ostatnią literę w napisie "Racecar" na i


napis = "Racecar"

print(napis[:6]+"i")

def replace_letter(napis, litera, pozycja= 3):
    if len(napis)>pozycja:
        napis=napis[:pozycja] + litera + napis[pozycja + 1:]

    return napis

print(replace_letter(napis,"Z"))