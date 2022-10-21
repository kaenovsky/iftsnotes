## wip

import sqlite3

bd = sqlite3.connect("database.db")
print("base de datos abierta")

cur = bd.cursor()

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Empleados
            (id int PK AI not NULL, numero_legajo int AI not NULL unique, dni_empleado int not NULL unique, nombre_empleado text not NULL, apellido_empleado text not NULL, area text not NULL)''')
    bd.commit()
    bd.close()
except:
    print('ocurrió un error')