class  carrera:
    __codCarrera: int
    __nombre: str
    __grado: str
    __duracion: str
    __tituloQueOtorga: str
    __codFacultad: int
    def __init__(self,codCarrera,nombre,grado,duracion,titulo,codF):
        self.__codCarrera= codCarrera
        self.__nombre= nombre
        self.__grado=grado
        self.__duracion=duracion
        self.__tituloQueOtorga=titulo
        self.__codFacultad= codF
        
    def __str__(self):
        return (f"Carrera: {self.__codCarrera} | "
                f"Nombre: {self.__nombre} | "
                f"Grado: {self.__grado} | "
                f"Duración: {self.__duracion} | "
                f"Título: {self.__tituloQueOtorga} | "
                f"Código Facultad: {self.__codFacultad}")
    
    def getCodCarrera(self):
        return self.__codCarrera
    def getNombre(self):
        return self.__nombre
    def getGrado(self):
        return self.__grado
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__tituloQueOtorga
    def getCodFacultad(self):
        return self.__codFacultad
    
    def __lt__(self,other):
        return self.__nombre < other.getNombre()