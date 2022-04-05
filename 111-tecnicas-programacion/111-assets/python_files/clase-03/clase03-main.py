print("repaso clase 02")

radio = float(input("ingrese el radio: "))

if radio > 0 and radio < 100:
    sup = 3.14 * radio * radio
    print("La superficie es: {}".format(sup))
else:
    print("error!")

print("# - fin - #")