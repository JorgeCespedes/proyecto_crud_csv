from clases.personal import *
from metodos import *
from check_input import *


def menu():

    while True:
        try:
            op = int(input('''
        Selecciona una opción:
            [1] Ingresa personal
            [2] Listar personal
            [3] Modificar personal
            [4] Borrar personal
            [5] Salir
        '''))

            if op == 1:
                codigo = check_codigo()
                nombre = check_nombre()
                edad   = check_edad()
                cargo  = check_cargo()

                personal = Personal(codigo,nombre, edad, cargo)
                ingresar_personal(personal)

            elif op == 2:
                listar_personal()

            elif op == 3:
                listar_personal()
                code = int(input('    Codigo a modificar: '))
                modificar_personal(code)

            elif op == 4:
                listar_personal()
                code = int(input('    Codigo a borrar: '))
                borrar_personal(code)

            elif op == 5:
                quit()

            else:
                print('Opción no válida.')

        except ValueError:
            print('Debe escoger una opción válida.')

