x = "Mielonka"

#def func():
#    print(x)
#func()

#def func():
 #   x = "NI!"
#func()
#print(x)

#def func():
 #   global x
 #   x = "NI"
#func()
#print(x)

#def func():
#    x = 'NI!'
#    print(x)
#func()
#print(x)

def func():
    x = "NI!"
    def nested():
        print(x)
    nested()

func()
print(x)
