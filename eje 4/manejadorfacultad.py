import csv
import numpy as np
from facultad import facultad
class manejadorFacultad:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __arreglo: np.ndarray
    def __init__(self, dimension=10, incremento=1):
        self.__arreglo = np.empty(dimension, dtype=facultad)
        self.__cantidad = 0
        self.__dimension = dimension

    def cargar(self):
        with open("eje 4/Facultades.csv", 'r', encoding='UTF-8') as archivoCarreras:
            reader = csv.reader(archivoCarreras, delimiter = ";")
            next(reader)
            for fac in reader:
                    unaFacultad = facultad(int(fac[0]), fac[1], fac[2], fac[3], ((fac[4])))
                    self.agregarFacultad(unaFacultad)
        print("Facultades cargadas:")
        for i in range(self.__cantidad):
            print(f"- {self.__arreglo[i].getNombre()}")

    def mostrar(self):
         for i in range(self.__cantidad):
              print(self.__arreglo[i])

    def agregarFacultad(self, unaFacultad):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension,refcheck=False)
        self.__arreglo[self.__cantidad]=unaFacultad
        self.__cantidad += 1
    
    def buscarFacultad(self,codFacultad):
        i=0
        while i< self.__cantidad and self.__arreglo[i].getCodFacultad() != codFacultad:
            i+=1
        if i < self.__cantidad:
             return self.__arreglo[i].getNombre()
    
    def contarCarreras(self,MC):
        
        for i in range(self.__cantidad):
            MC.contarCarrerasEnMC(self.__arreglo[i].getCodFacultad())
        
    def listarCarreras(self,nomF,MC):
        i=0
        while i< self.__cantidad and self.__arreglo[i].getNombre() != nomF:
            i+=1
        if i< self.__cantidad:
            MC.listarCarreras(self.__arreglo[i].getCodFacultad())
