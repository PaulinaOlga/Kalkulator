# Program, który przypomina o piciu wody co 30 minut (od kliknięcia przycisku).
# Przypominajkę można odłożyć (po kliknięciu odpowiedniego przyciusku) na 5 minut
import time
#from datetime import datetime
from tkinter import *
from PIL import ImageTk

def zamknij_okno(czas):
    top.withdraw()
    time.sleep(czas)
    top.deiconify()

def zamknij_okno5():
    zamknij_okno(5*60)

def zamknij_okno30():
    zamknij_okno(30*60)

def pokaz_okno():
    top.title("Przypominajka")
    top.geometry("300x300")
    top.configure(bg="Black")
    wiadomosc = "Napij się"
    napis = Label(top, text=wiadomosc, font="Arial 10")
    napis.pack()        #zobacz jakie elementy dodaliśmy
    #dodaje obraz
    canvas = Canvas(top, bg="Black", width=200, height=210)
    canvas.pack()
    img = ImageTk.PhotoImage(file="glass.jpg")
    canvas.create_image(20, 20, anchor=NW, image=img)
    #dodaje przycisk
    button = Button(top, text="Napiłam się", fg="Black", bg="White", command=zamknij_okno30)
    button.pack()
    button2 = Button(top, text="Przypomnij mi za 5 minut", fg="Black", bg="White", command=zamknij_okno5)
    button2.pack()
    top.mainloop()       # uruchom system okien



top = Tk()
pokaz_okno()