import numpy as np
import csv
from colectivo import colectivo

class gestorColectivo:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __arreglo: np.ndarray
    def __init__(self, dimension=10, incremento=1):
        self.__arreglo = np.empty(dimension, dtype=colectivo)
        self.__cantidad = 0
        self.__dimension = dimension

    def cargar(self):
        with open("colectivos.csv", 'r', encoding='UTF-8') as archivoColectivo:
            reader = csv.reader(archivoColectivo, delimiter=";")
            next(reader)  
            for colec in reader:
                unColectivo = colectivo(colec[0],colec[1],colec[2],colec[3],colec[4])

                self.agregar(unColectivo)
        print("colectivos cargados")

        for i in range(self.__cantidad):
            print(f"- {self.__arreglo[i].getDniChofer()}")

        
    def agregar(self, unColectivo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)  # Agregado 'refcheck=False'
        self.__arreglo[self.__cantidad] = unColectivo
        self.__cantidad += 1

    def buscarChofer(self,dni):
        i=0
        while i < (self.__cantidad) and dni != self.__arreglo[i].getDniChofer():
            i+=1
        if i < (self.__cantidad):
            return self.__arreglo[i].getPatente()
        
    def recorrerColectivos(self,GT):
        
        for cole in self.__arreglo:
            if cole is not None:  # Evitás el error
                GT.calcularDistancia(cole.getPatente(), cole.getConsumoPromedio())
