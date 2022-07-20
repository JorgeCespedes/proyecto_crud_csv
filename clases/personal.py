
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
