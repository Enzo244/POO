from habitacion import habitacion
class hotel:
    __nombre: str
    __pais: str
    __provincia:str
    __direccion:str
    __listaHabitaciones: list

    def __init__(self, nombre, direc, tel):
        self.__nombre= nombre
        self.__direccion=direc
        self.__telefono=tel
        self.__listaHabitaciones= []
    
    def getNombre(self):
        return self.__nombre
    def agregar(self,numero,piso,tipoH,precio,disp):
        unaHabitacion= habitacion(numero,piso,tipoH,precio,disp)
        self.__listaHabitaciones.append(unaHabitacion)