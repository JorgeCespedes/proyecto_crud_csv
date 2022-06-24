import random


def check_codigo():
    codigo = random.randint(1000,9999)
    codigo = int(codigo)
    return codigo


def check_nombre():
    while True:
        try:
            nombre = input('Ingresa el nombre: ')
            nombre = nombre.replace(' ','')
            nombre = nombre.capitalize()
        except:
            print('Ingresa un nombre: ')
            continue

        if len(nombre) <= 0:
            print('Ingresa un nombre.')
            continue
        else:
            break

    return nombre


def check_edad():
    while True:
        try:
            edad = int(input('Ingresa la edad: '))
        except ValueError:
            print('Ingresa una edad válido')
            continue

        if edad <= 0:
            print('Ingresa una edad positiva.')
            continue
        else:
            break

    return edad


def check_cargo():
    cargo = 'Sin cargo'
    
    try:
        op = int(input('''
    Escoge el cargo: 
        [1] Obrero
        [2] Tecnico
        [3] Administrativo
        '''))

        if op == 1:
            cargo = 'Obrero'
        elif op == 2:
            cargo = 'Tecnico'
        elif op == 3:
            cargo = 'Administrativo'
        else:
            print('Opción no válida.')

    except ValueError:
        print('Ingresa una ópción válida.')

    return cargo

