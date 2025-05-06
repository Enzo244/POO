class Paciente:
    def __init__(self, dni, nombre, unidad):
        self.__dni = dni
        self.__nombre = nombre
        self.__unidad = unidad

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_unidad(self):
        return self.__unidad

    def __str__(self):
        return f'DNI: {self.__dni}, Nombre: {self.__nombre}, Unidad: {self.__unidad}'
