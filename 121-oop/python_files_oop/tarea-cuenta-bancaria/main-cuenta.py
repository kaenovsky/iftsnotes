from abc import ABC, abstractmethod

# definimos la clase concreta Cliente

class Cliente():
    def __init__(self, razon_social, cuil, domicilio):
        print('Inicializando instancia Cliente (...)')
        self.razon_social = razon_social
        self.cuil = cuil
        self.domicilio = domicilio

    # definimos propiedades getter y setter de los atributos de instancia Cliente

    @property
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self, value):
        self.__razon_social = value

    @property
    def cuil(self):
        return self.__cuil

    @cuil.setter
    def cuil(self, value):
        self.__cuil = value

    @property
    def domicilio(self):
        return self.__domicilio

    @domicilio.setter
    def domicilio(self, value):
        self.__domicilio = value

    # definimos el método crear cuenta de un cliente

    def crear_cuenta_bancaria(self, tipo_cuenta, nro_cuenta, titular, saldo) -> bool:
        if tipo_cuenta == 'CA':
            return CajaAhorro(nro_cuenta, titular, saldo)
        elif tipo_cuenta == 'CC':
            return CuentaCorriente(nro_cuenta, titular, saldo)        

# definimos la clase abstracta cuenta bancaria

class CuentaBancaria(ABC):
    def __init__(self, nro_cuenta:int, titular:Cliente, saldo:float):
        print('Inicializando instancia CuentaBancaria (...)')
        self.nro_cuenta = nro_cuenta
        self.titular = titular
        self.saldo = saldo

    # definimos propiedades getter y setter de los atributos de instancia CuentaBancaria

    @property
    def nro_cuenta(self):
        return self.__nro_cuenta

    @nro_cuenta.setter
    def nro_cuenta(self, value):
        self.__nro_cuenta = value

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        self.__titular = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    # definimos métodos de instancia 

    def consultar_saldo(self) -> float:
        print('Consultando el saldo')
        return self.__saldo

    def depositar(self, monto_depositar) -> bool:
        self.saldo = self.saldo + monto_depositar

    def consultar_cliente(self) -> str:
        return 'el cliente es: ' + self.__titular
    
    # definimos métodos abstractos

    @abstractmethod
    def extraer(monto_extraer) -> bool:
        pass

    @abstractmethod
    def transferir(monto_transferir) -> bool:
        pass

# definimos la clase concreta caja ahorro

class CajaAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, titular, saldo, limite_extracciones:float=50000, cant_extracciones:float=10):
        super().__init__(nro_cuenta, titular, saldo) 
        print('Inicializando instancia CajaAhorro (...)')
        self.limite_extracciones = limite_extracciones
        self.cant_extracciones = cant_extracciones

    # definimos propiedades getter y setter de los atributos de instancia CajaAhorro

    @property
    def limite_extracciones(self):
        return self.__limite_extracciones

    @limite_extracciones.setter
    def limite_extracciones(self, value):
        self.__limite_extracciones = value

    @property
    def cant_extracciones(self):
        return self.__cant_extracciones

    @cant_extracciones.setter
    def cant_extracciones(self, value):
        self.__cant_extracciones = value

    # definimos el método crear cuenta de caja de ahorro

    def extraer(self, monto_extraer) -> bool:
        if monto_extraer > self.saldo or monto_extraer > self.limite_extracciones:
            print('Error, no puede extraer ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_extraer
            print('Extracción exitosa')
            return True            

    def transferir(self, monto_transferir) -> bool:
        if monto_transferir > self.saldo:
            print('Error, no puede transferir ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_transferir
            print('Transferencia exitosa')
            return True

# definimos la clase concreta cuenta corriente

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, titular, saldo, monto_descubierto:float=50000):
        super().__init__(nro_cuenta, titular, saldo)
        print('Inicializando instancia CuentaBancaria (...)')
        self.monto_descubierto = monto_descubierto

    # definimos propiedades getter y setter de los atributos de instancia CuentaCorriente

    @property
    def monto_descubierto(self):
        return self.__monto_descubierto

    @monto_descubierto.setter
    def monto_descubierto(self, value):
        if value > 0:
            self.__monto_descubierto = value
        else:
            print('No se puede asignar un valor negativo al monto en descubierto')

    # definimos el método crear cuenta de caja de ahorro

    def extraer(self, monto_extraer) -> bool:
        if monto_extraer > self.saldo + self.monto_descubierto:
            print('Error, no puede extraer ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_extraer
            print('Extracción exitosa')
            return True
    
    def transferir(self, monto_transferir) -> bool:
        if monto_transferir > self.saldo + self.monto_descubierto:
            print('Error, no puede transferir ese monto')
            return False
        else:
            self.saldo = self.saldo - monto_transferir
            print('Transferencia exitosa')
            return True

def main():
    c1 = Cliente('Conglom-o', 20922929, 'Zapiola 2021')
    print(c1)

    cuenta1 = c1.crear_cuenta_bancaria('CA', 20010, c1, 2)
    cuenta2 = c1.crear_cuenta_bancaria('CC', 20010, c1, 30)

    print('Saldo actual: ', cuenta1.consultar_saldo())
    cuenta1.depositar(500920)
    print('Saldo actual CA: ', cuenta1.consultar_saldo())
    cuenta1.extraer(50022920)
    print('Saldo actual CA: ', cuenta1.consultar_saldo())
    
    print('Saldo actual CC: ', cuenta2.consultar_saldo())
    cuenta2.monto_descubierto = -300
    #cuenta2.extraer(400)
    print('Saldo actual CC: ', cuenta2.consultar_saldo())
    cuenta2.transferir(580)
    print('Saldo actual CC: ', cuenta2.consultar_saldo())

main()