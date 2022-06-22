from clases import *
import csv
from csv import writer
from csv import reader


def ingresar_personal(personal):

    list_data = personal.descripcion()

    with open('archivo.csv', 'a', newline='') as f_archivo:
        writer_object = writer(f_archivo)
        writer_object.writerow(list_data)
        f_archivo.close()

    print('Agregado correctamente.')


def listar_personal():
    print('Listar Personal')

    with open('archivo.csv', 'r') as f_archivo:
        archivo_csv = reader(f_archivo, delimiter=',')
        header = next(archivo_csv)
        print("*"*35)
        print(", ".join(header))
        print("*"*35)

        for row in archivo_csv:
            print(', '.join(row))

        print("*"*35)



def borrar_personal():
    print('Borrar personal.')


    '''
    with open('archivo.csv', 'rb') as inp, open('new.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[2] != "0":
                writer.writerow(row)
    os.remove('archivo.csv')
    os.rename('new.csv', 'archivo.csv')

    '''

