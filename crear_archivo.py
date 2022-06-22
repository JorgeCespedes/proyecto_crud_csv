import csv
import os.path
from menu import *


def crear_archivo():
    if os.path.isfile('archivo.csv'):
      menu()
    else:
      with open('archivo.csv', 'w', newline='') as file:
        archivo = csv.writer(file, delimiter=',')
        header = ['codigo', 'nombre', 'edad', 'cargo']
        archivo.writerow(header)
      menu()
