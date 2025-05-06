class facultad:
    __codFacultad:int
    __nombre: str
    __direcccion: str
    __localidad: str
    __tel: int
    def __init__(self,codFacultad,nombre,direc,locals,tel):
        self.__codFacultad=codFacultad
        self.__nombre= nombre
        self.__direcccion= direc
        self.__localidad= locals
        self.__tel= tel
    def __str__(self):
        return(
            f"Codigo Facultad: {self.__codFacultad} |"
            f"nombre: {self.__nombre} |"
            f"direccion: {self.__direcccion} |"
            f"localidad {self.__localidad} |"
            f"telefono: {self.__tel}"
        )
    
    def getCodFacultad(self):
        return self.__codFacultad
    def getNombre(self):
        return self.__nombre
    def ggetDireccion(self):
        return self.__direcccion
    def getLocalidad(self):
        return self.__localidad
    def getTel(self):
        return self.__tel