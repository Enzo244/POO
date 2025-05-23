import numpy as np
import csv
from medico import Medico

class gestorMedico:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __arreglo: np.ndarray

    def __init__(self, dimension=10, incremento=1):
        self.__arreglo = np.empty(dimension, dtype=Medico)
        self.__cantidad = 0
        self.__dimension = dimension

    def cargar(self):
        with open("medicos.csv", 'r', encoding='UTF-8') as archivoMedicos:
            reader = csv.reader(archivoMedicos, delimiter=";")
            next(reader)  
            for medic in reader:
                unMedico = Medico(medic[0],medic[1],medic[2],medic[3],medic[4])

                self.agregar(unMedico)
        print("Medicos cargados")

        for i in range(self.__cantidad):
            print(f"- {self.__arreglo[i].getDni()}")

        
    def agregar(self, unMedico):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False) 
        self.__arreglo[self.__cantidad] = unMedico
        self.__cantidad += 1



    def mostrarPorCadaMedico(self,GV):

        for medic in self.__arreglo:
            if medic is not None:
                print(f"nombre completo : {medic.getNombre()}")
                print(f"especialidad: {medic.getEspecialidad()}")
                print(f"zona de cobertura: {medic.getZona()}\n")
                GV.totalVisitasRealizadas(medic.getDni(),medic.getValorVisita())


    def mostrarNombrePorDni(self,dni):
        i=0
        while i< self.__cantidad and self.__arreglo[i].getDni() != dni:
            i+=1
        if i< self.__cantidad:
            print(f"nombre del medico: {self.__arreglo[i].getNombre()}")