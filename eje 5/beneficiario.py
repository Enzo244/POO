class beneficiario :
    __dni: int
    __nombre: str
    __apellido: str
    __carrera: str
    __siglaFacultad:str
    __añoQueCursa: str
    __promedio: int
    __idBeca: int

    def __init__(self,dni,nombre,apellido,carrera,siglafacultad,añoquecursa,promedio,idbeca):
        self.__dni= dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__carrera=carrera
        self.__siglaFacultad=siglafacultad
        self.__añoQueCursa=añoquecursa
        self.__promedio=promedio
        self.__idBeca=idbeca
    
    def getDni(self):
        return self.__dni
    
    def getIdBeca(self):
        return self.__idBeca

    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return (f"Beneficiario [DNI: {self.__dni}, Nombre: {self.__nombre} {self.__apellido}, "
                f"Carrera: {self.__carrera}, Facultad: {self.__siglaFacultad}, Año: {self.__añoQueCursa}, "
                f"Promedio: {self.__promedio}, ID Beca: {self.__idBeca}]")