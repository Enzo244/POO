class beca:
    __idBeca: int
    __tipoBeca: str
    __importeBeca: float
    def __init__(self,idbeca,tipobeca,importebeca):
        self.__idBeca=idbeca
        self.__tipoBeca= tipobeca
        self.__importeBeca= importebeca
    
    def getIdBeca(self):
        return self.__idBeca

    def getTipoBeca(self):
        return self.__tipoBeca
    
    def getImporte(self):
        return self.__importeBeca
    
    def __str__(self):
        return f"Beca [ID: {self.__idBeca}, Tipo: {self.__tipoBeca}, Importe: ${self.__importeBeca:.2f}]"