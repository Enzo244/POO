class tramo:
    __ciudadOrigen: str
    __ciudadDestino:str
    __distanciaEnKm: float
    __patenteColectivo: str
    def __init__(self,ciudadorigen,ciudaddestino,distanciaenkm,patentecolectivvo):
        self.__ciudadOrigen=ciudadorigen
        self.__ciudadDestino=ciudaddestino
        self.__distanciaEnKm= float(distanciaenkm)
        self.__patenteColectivo=patentecolectivvo
    
    def getPatente(self):
        return self.__patenteColectivo
    def getCiudadOrigen(self):
        return self.__ciudadOrigen
    def getCiudadDestino(self):
        return self.__ciudadDestino
    def getDistancia(self):
        return self.__distanciaEnKm
    
    def __gt__(self, otra_distancia):
        return self.__distanciaEnKm > otra_distancia