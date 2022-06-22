from csv import writer


class Personal:
    def __init__(self, codigo, nombre, edad, cargo):
        self.codigo = codigo
        self.nombre = nombre
        self.edad   = edad
        self.cargo  = cargo
        self.lista_personal = []

    def descripcion(self):
        self.lista_personal = [ self.codigo,self.nombre, self.edad, self.cargo ]
        return self.lista_personal


def ingresar_personal(personal):
    
    print('Ingresar Personal')

    list_data = personal.descripcion()

    with open('menu.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()

    print('Agregado correctamente.')


def listar_personal():
    print('Listar Personal')


def borrar_personal():
    print('Borrar personal.')




def menu():
    
    try: 
        op = int(input('''
        Selecciona una opción:
            [1] Ingresa personal
            [2] Listado de personal
            [3] Borrar personal
            [4] Salir
        '''))

        if op == 1:
            codigo = input('Código : ')
            nombre = input('Nombre : ')
            edad   = input('Edad   : ')
            cargo  = input('Cargo  : ')

            personal = Personal(codigo,nombre, edad, cargo)

            ingresar_personal(personal)

        elif op == 2:
            listar_personal()
    
        elif op == 3:
            borrar_personal()

        elif op == 4:
            quit()

        else:
            print('Opción no válida.')
    
    except ValueError:
        print('Debe escoger una opción válida.')





if __name__ == '__main__':
    menu()

