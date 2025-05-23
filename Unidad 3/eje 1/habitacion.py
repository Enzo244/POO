class habitacion:
    __numero: int
    __piso: int
    __tipoDeHabitacion: str
    __precioPorNoche: float
    __disponibilidad: bool
    
    def __init__(self,num,piso,tipo,precio,disp):
        self.__numero=num
        self.__piso=piso
        self.__tipoDeHabitacion=tipo
        self.__precioPorNoche=precio
        self.__disponibilidad=disp

        