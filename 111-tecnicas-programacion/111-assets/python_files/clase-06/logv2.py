## clase 06 - while loop

print("~~~~~ inicio del programa ~~~~~")
print()

user = "low@raw.cc"
passw = "locked"
error = 0
maxError = 3

while (maxError > error):

    userInput = input("Ingrese user: ")
    passwInput = input("Ingrese pass: ")

    if userInput == user:
        if passwInput == passw:            
            print("El user y la pass coinciden")
            break
        else:
            print("error en passwd")
            error = error + 1
    else:
        print("error en user")
        error = error + 1

if error == maxError:
    print("demasiados intentos erroneos!")
else:
    print("Hola {} tu ingreso fue correcto. Eso es todo.".format(user))
    
print()
print("~~~~~ fin del programa ~~~~~")