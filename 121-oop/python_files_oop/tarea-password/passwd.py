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
        numbers = 0
        for i in self.password:
            if(i.isdigit()):
                numbers = numbers + 1
            if(i.isupper()):
                mayus = mayus + 1
            if(i.islower()):
                minus = minus + 1
        
        if mayus >= 2 and minus >= 1 and numbers > 5:
            return True
        else:
            return False

    def makePassword(self):
        return (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.__longitud)))

    def __str__(self) -> str:
        return self.password + ' - ' + str(self.isStrong())

def main():
    passwordsList = []
    pass1 = Password(5)
    pass2 = Password(56)
    passwordsList.append(pass1)
    passwordsList.append(pass2)
    
    for i in passwordsList:
        print(i)

main()