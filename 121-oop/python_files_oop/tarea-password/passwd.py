import string
import random

class Password():
    # atributo de clase
    LONGITUD = 8

    # método inicializador
    def __init__(self, longitud=LONGITUD):
        print('Inicializando instancia password (...)')
        self.longitud = longitud
        self.password = self.makePassword()

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, value):
        self.__longitud = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def isStrong(self) -> bool:
        mayus = 0
        minus = 0
        numbs = 0
        for i in self.password:
            if(i.isdigit()):
                numbs = numbs + 1
            if(i.isupper()):
                mayus = mayus + 1
            if(i.islower()):
                minus = minus + 1
        
        if mayus >= 2 and minus >= 1 and numbs > 5:
            return True
        else:
            return False

    def makePassword(self):
        return (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.__longitud)))

    def __str__(self) -> str:
        if self.isStrong():
            res = 'La pass es fuerte [✓]'
        else:
            res = 'La pass no es fuerte [✕]'

        return self.password + ' - ' + res

def main():
    
    passwordsList = []
    cond = True

    # Pedimos ingresar por teclado cantidad de caracteres

    while(cond):
        
        print('Ingrese un número de cantidade caracteres.\nSi ingresa 0 se usará el valor por defecto')
        
        chars = int(input('Cantidad de caracteres: '))
        if (chars == 0):
            passwd = Password()
        else:
            passwd = Password(chars)

        passwordsList.append(passwd)        
        
        response = input('Desea ingresar otra longitud de contraseña?: [s/n] ')
        
        while(response != "n" and response != "N" and response != "s" and response != "S"):
            print('(!) error: Responda sí o no')
            response = input('Desea ingresar otra longitud de contraseña?: [s/n] ')

        # Si el usuario ingresa N cambiamos la condición a False y salimos del bucle
        if(response == 'n' or response == 'N'):
            cond = False

    # Fuera del bucle, iteramos passwordsList mostrando las contraseñas y si son fuertes

    i = 1

    for p in passwordsList:
        print()
        print('Contraseña nro {}:'.format(i))
        print(p)
        print()
        i = i + 1

main()