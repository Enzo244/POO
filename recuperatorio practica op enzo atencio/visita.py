class Visita:
    __fecha: str
    __dniPaciente: int
    __zona: str
    __dniMedico: int
    __diagnostico: str

    def __init__(self, fecha, dniPaciente, zona, dniMedico, diagnostico):
        self.__fecha = fecha
        self.__dniPaciente = dniPaciente
        self.__zona = zona
        self.__dniMedico = dniMedico
        self.__diagnostico = diagnostico

    def getFecha(self):
        return self.__fecha

    def getDniPaciente(self):
        return self.__dniPaciente

    def getZona(self):
        return self.__zona

    def getDniMedico(self):
        return self.__dniMedico

    def getDiagnostico(self):
        return self.__diagnostico

    def __eq__(self, otra_zona):
        if isinstance(otra_zona, str):
            return self.__zona == otra_zona
        return False
