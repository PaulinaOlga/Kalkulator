mama= 1
tata = 2
kot= 3
suma= 0
def suma_zebranych_jablek(a,b,c):
    suma= a+b+c
    return(suma)

sumaJablek= suma_zebranych_jablek(mama, tata, kot)

if sumaJablek > 0:
    print("brawo")
else:
    print("no to słabo")