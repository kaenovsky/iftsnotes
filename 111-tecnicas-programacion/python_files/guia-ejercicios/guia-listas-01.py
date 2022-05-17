"""
Escribir una función que calcule el total 
de una factura tras aplicarle el IVA. La 
función debe recibir la cantidad sin IVA 
y el porcentaje de IVA a aplicar, y devolver 
el total de la factura. Si se invoca la 
función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.
"""
print("~~~~~ inicio del programa ~~~~~")
print()

ivaFinal = 0
line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print(line)
print("$$ Vamos a obtener el costo de su factura final $$")
print(line)

montoNeto = float(input("Ingrese el monto de su factura: "))
while(montoNeto <= 0):
    print("(!) error: ingrese un monto mayor a 0")
    montoNeto = float(input("Vuelva a ingresar el monto de su factura: "))    
print(line)
print("Opcionalmente, puede customizar su porcentaje de IVA.")
print("[!] Si indica 0, el monto será 21% por defecto.")
print(line)
ivaCustom = int(input("Si corresponde, ingrese ahora el porcentaje de IVA personalizado: "))
while(ivaCustom < 0):
    print("(!) error: ingrese un monto mayor a 0")
    ivaCustom = int(input("Vuelva a ingresar IVA personalizado: ")) 
print(line)

def calcIva(montoNeto, ivaCustom):
    print("El monto de su factura sin IVA es ${:.2f}".format(montoNeto))
    if(ivaCustom != 0):
        ivaFinal = montoNeto * ivaCustom / 100 
        montoTotal = montoNeto + ivaFinal
        print("El porcentaje de IVA es %{:.0f}".format(ivaCustom))
        print("El monto de IVA es: ${:.2f}".format(ivaFinal))
        print(line)
        print("El monto total a abonar es: ${:.2f}".format(montoTotal))
        print(line)        
    else:
        ivaDefault = montoNeto * 21 / 100
        montoTotal = montoNeto + ivaDefault
        print("El porcentaje de IVA es %21")
        print("El monto de IVA es: ${:.2f}".format(ivaDefault))
        print(line)
        print("El monto total a abonar es: ${:.2f}".format(montoTotal))
        print(line)

## llamo función calcIva
calcIva(montoNeto, ivaCustom)

print()
print("~~~~~ fin del programa ~~~~~")