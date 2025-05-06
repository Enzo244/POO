class Atencion:
    def __init__(self, dni, fecha, importe):
        self.__dni = dni
        self.__fecha = fecha
        self.__importe = float(importe)

    def get_dni(self):
        return self.__dni

    def get_fecha(self):
        return self.__fecha

    def get_importe(self):
        return self.__importe

    def __str__(self):
        return f'DNI: {self.__dni}, Fecha: {self.__fecha}, Importe: ${self.__importe:.2f}'
