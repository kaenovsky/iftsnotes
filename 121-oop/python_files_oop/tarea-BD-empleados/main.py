import sqlite3

def conn_db():
    db = sqlite3.connect('database.db')
    return db

def create_table(cur):
    cur.execute('''
            CREATE TABLE IF NOT EXISTS `Empleados` (
            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            `numero_legajo`	INTEGER NOT NULL,
            `dni_empleado`	INTEGER NOT NULL,
            `nombre_empleado`	TEXT,
            `apellido_empleado`	TEXT,
            `area`	TEXT
            );    
        ''')
    db.commit()

def add_user(cur, values):
    conn_db()
    cur.execute('INSERT INTO Empleados VALUES(?,?,?,?,?,?)',values)
    print('Se ingresó un nuevo empleado')
    db.commit()

def select_user(cur, dni):
    conn_db()
    print('A continuación verá el registro del empleado: ')
    cur.execute('SELECT * FROM Empleados WHERE dni_empleado = ?', [dni])
    print(cur.fetchone())

def select_all(cur):
    conn_db()
    cur.execute('SELECT * FROM Empleados')
    print(cur.fetchall())

def change_user(cur, nro_leg, area):
    conn_db()
    cur.execute('UPDATE Empleados SET area = ? WHERE numero_legajo = ? ', [area, nro_leg])
    print('Se modificó un registro de empleado')
    db.commit()

def delete_user(cur, nro_leg):
    conn_db()
    cur.execute('DELETE FROM Empleados WHERE numero_legajo = ?', [nro_leg])
    print('Se eliminó un registro de empleado')
    db.commit()

db = conn_db()
cur = db.cursor()
create_table(cur)

def main():
    
    cond = True

    while cond == True:
        print('ingrese la opcion que desea ejecutar ')
        print('Opción 1: Insertar un registro de empleado')
        print('Opción 2: Seleccionar un registro de empleado a partir de su número de DNI')
        print('Opción 3: Seleccionar todos los empleados o los registros de la tabla')
        print('Opción 4: Modificar el área de un empleado en función de su número de legajo')
        print('Opción 5: Eliminar un empleado a partir de su número de legajo')
        print('Opción 6: Finalizar')

        opt = int(input('Ingrese la opción seleccionada: '))

        if opt == 1:
            conn_db()
            values = []
            print('Opción 1: Ingresar empleado. A continuación ingrese los datos del empleado a cargar.')
            val1 = int(input('Ingrese Nro de ID del empleado: '))
            values.append(val1)
            val2 = int(input('Ingrese Nro de legajo del empleado: '))
            values.append(val2)
            val3 = int(input('Ingrese DNI del empleado: '))
            values.append(val3)
            val4 = (input('Ingrese nombre del empleado: '))
            values.append(val4)
            val5 = (input('Ingrese apellido del empleado: '))
            values.append(val5)
            val6 = (input('Ingrese área en donde trabaja el empleado: '))
            values.append(val6)

            add_user(cur, values)

        elif opt == 2:
            conn_db()
            print('Opción 2: Mostrar registro de empleado. A continuación ingrese un DNI para ver el registro del empleado correspondiente.')
            dni = int(input('Ingrese número de DNI: '))

            select_user(cur, dni)

        elif opt == 3:
            conn_db()
            print('Opción 3: Mostrar todos los registros de empleados.')
            
            select_all(cur)

        elif opt == 4:
            conn_db()
            print('Opción 4: Modificar area de empleado. Ingresará el número de legajo del empleado y el área a modificar.')
            nro_leg = int(input('Ingrese el número de legajo del empleado a modificar: '))
            area = input('Ingrese un área nueva para asignar a este empleado: ')
            change_user(cur, nro_leg, area)

        elif opt == 5:
            conn_db()
            print('Opción 5: Eliminar registro de empleado. Ingrese el número de legajo del empleado a eliminar.')
            nro_leg = int(input('Ingrese el número de legajo del empleado a eliminar: '))
            delete_user(cur, nro_leg)

        elif opt == 6:
            cond = False
            db.close()
            print('Saliendo del programa')

main()