from clases import *
from check_input import *
import csv
from csv import writer
from csv import reader
from clases.personal import *


def ingresar_personal(personal):
    list_data = personal.descripcion()

    with open('archivo.csv', 'a', newline='') as f_archivo:
        writer_object = writer(f_archivo)
        writer_object.writerow(list_data)
        f_archivo.close()

    print('Personal agregado correctamente.')


def listar_personal():
    print('Listado de Personal')

    with open('archivo.csv', 'r') as data:
        archivo_csv = reader(data, delimiter=',')

        print('*'*35)
        for row in archivo_csv:
            print(', '.join(row))
        print("*"*35)



def borrar_personal(code):
    print('Borrar personal.')

    code = str(code)
    lista_datos = []

    with open('archivo.csv', 'r') as data:
        archivo_csv = reader(data, delimiter=',')
        for row in archivo_csv:
            lista_datos.append((row))

    for item in lista_datos:
        for elem in item:
            if elem == code:
                posicion = lista_datos.index(item)

    lineToSkip = posicion 
    with open('archivo.csv','r') as read_file:
        lines = read_file.readlines()

    currentLine = 0
    with open('archivo.csv','w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)	
            currentLine += 1
    print('Se eliminó correctamente.')


def modificar_personal(code):
    print('Modificar personal')

    code = str(code)
    lista_datos = []

    with open('archivo.csv', 'r') as data:
        archivo_csv = reader(data, delimiter=',')
        for row in archivo_csv:
            lista_datos.append((row))

    for item in lista_datos:
        for elem in item:
            if elem == code:
                nombre = item[1]
                edad   =  item[2]
                cargo  = item[3]
    
    codigo = code
    nombre = check_nombre()
    edad  = check_edad()
    cargo = check_cargo()
    
    borrar_personal(code)

    personal = Personal(codigo, nombre, edad, cargo)
    ingresar_personal(personal)
        
