class colectivo:
    __patente: str
    __marca: str
    __modelo: str
    __capacidad: int
    __dniChofer: int
    __consumoPromedioColectivo=35
    def __init__(self,patente,marca,modelo,capacidad,dnichofer):
        self.__patente=patente
        self.__marca=marca
        self.__modelo=modelo
        self.__capacidad=capacidad
        self.__dniChofer=dnichofer
    
    def getDniChofer(self):
        return self.__dniChofer
    def getPatente(self):
        return self.__patente
    def getConsumoPromedio(self):
        return self.__consumoPromedioColectivo