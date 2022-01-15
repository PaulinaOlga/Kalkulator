#a= 5
#b= 8
#c= 11
#suma= 0
#suma= a+b+c

#print ("obwód trójkąta: " + str(suma))

w = int(input("Podaj 1 długość: "))
e= int(input("Podaj 2 długość: "))
r = int(input("Podaj 3 długość: "))

def podaj_dlugosci(a,b,c):
    obw = a+b+c
    print("obwód wynosi: " + str(obw))

podaj_dlugosci(w,e,r)

#bok1 = 5
#bok2 = 8
#bok3 = 11

#podaj_dlugosci(bok1,bok2,bok3)

#dl1 = 6
#dl2 = 10
#dl3 = 14

#podaj_dlugosci(dl1,dl2,dl3)

def moj_print(x):
    print(x)

moj_print("lol")
