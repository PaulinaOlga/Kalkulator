import math


def dodaj(a, b):
    return a + b


def odejmij (a,b):
    return a - b

def pomnoz(a,b):
    return a * b

def podziel(a, b):
    return a / b

def sinus(x):
    return math.sin(x)

#def pierwiastek (a, b):  # lub to poniżej
    #return a ** b

def pierwiastek (x):
    return math.sqrt(x)

def kwadrat (x):
    return x*x

def objetoscWalca (r,h,pi=3.14):
    V = pi*h*kwadrat(r)
    return V



def poleTrojkata (a,h):
    return a * h * 0.5
