print(" === $$$ clase 04 $$$ ===")

user = "low@raw.cc"
passw = "locked"

userInput = input("Ingrese user: ")
passwInput = input("Ingrese pass: ")

if userInput == user:
    if passwInput == passw:
        print("Ingreso ok! Hola {}".format(user))
    else:
        print("error en passwd")
else:
    print("error en user") 

print("# - fin - #")