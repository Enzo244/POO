class Medico:
    __dni: int
    __nombreCompleto: str
    __especialidad: str
    __matricula:str
    __zona: str
    __valorVisita = 14500  


    def __init__(self, dni, nombreCompleto, especialidad, matricula, zona):
        self.__dni = dni
        self.__nombreCompleto = nombreCompleto
        self.__especialidad = especialidad
        self.__matricula = matricula
        self.__zona = zona

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombreCompleto

    def getEspecialidad(self):
        return self.__especialidad

    def getZona(self):
        return self.__zona

    @classmethod
    def getValorVisita(cls):
        return cls.__valorVisita
