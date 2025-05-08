from atencion import Atencion
import numpy as np
import csv

class gestorAtencion:
    __arregloAtencion: np.array
    __cantidad:int
    __dimension: int
    __incremento= 5
    def __init__(self,dimension=10,incremento=5):
        self.__arregloAtencion= np.empty(dimension,dtype=Atencion)
        self.__cantidad=0
        self.__dimension= dimension
    
    def cargar(self):
        with open("atenciones.csv",'r' ,encoding="utf-8") as archivoAten:
            reader= csv.reader(archivoAten, delimiter=";")
            next(reader)

            for aten in reader:
                unaAten=Atencion(aten[0],aten[1],aten[2])
                self.agregarPunto(unaAten)

    def agregarPunto(self, unaAt):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloAtencion.resize(self.__dimension)
        self.__arregloAtencion[self.__cantidad]=unaAt
        self.__cantidad += 1
    
    def mostrar(self):
        for at in range(self.__cantidad):
            print(at)