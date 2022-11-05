import csv
import os.path
from menu import *

def crear_archivo():
    if not os.path.isfile('archivo.csv'):
      with open('archivo.csv', 'w', newline='') as file:
        archivo = csv.writer(file, delimiter=',')
        header = ['codigo', 'nombre', 'edad', 'cargo']
        archivo.writerow(header)
    menu()

