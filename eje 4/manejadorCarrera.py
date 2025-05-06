import csv
import numpy as np
from carrera import carrera

class manejadorCarrera:
    __cantidad: int
    __dimension: int
    __incremento = 5
    __arreglo: np.ndarray
    def __init__(self, dimension=10, incremento=1):
        self.__arreglo = np.empty(dimension, dtype=carrera)
        self.__cantidad = 0
        self.__dimension = dimension

    def cargar(self):
        with open("eje 4/Carreras.csv", 'r', encoding='UTF-8') as archivoCarreras:
            reader = csv.reader(archivoCarreras, delimiter=";")
            next(reader)  # Saltar la cabecera
            for carr in reader:
                unaCarrera = carrera(int(carr[0]), carr[1], carr[2], carr[3], carr[4], int(carr[5]))
                self.agregarCarreras(unaCarrera)
        print("Carreras cargadas:")
        for i in range(self.__cantidad):
            print(f"- {self.__arreglo[i].getNombre()}")

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__arreglo[i])
        
    def agregarCarreras(self, unaCarrera):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension, refcheck=False)  # Agregado 'refcheck=False'
        self.__arreglo[self.__cantidad] = unaCarrera
        self.__cantidad += 1

    def BuscarCarrera(self,nomCarrera,MF):
        i=0
        while i < self.__cantidad and self.__arreglo[i].getNombre().lower()  !=  nomCarrera.lower():
            i+=1
        if i < self.__cantidad:
            codFacultad= self.__arreglo[i].getCodFacultad()
            nombreFacultad=MF.buscarFacultad(codFacultad)
            print(f"este es el nombre de la facultad: {nombreFacultad}")
    
    def contarCarrerasEnMC(self,codF):
        cont=0
        for carrera in self.__arreglo:
            if codF == carrera.getCodFacultad():
                cont+=1
        print(f"{cont}")
    
    def listarCarreras(self,codF):

        for i in range(self.__cantidad):

            if self.__arreglo[i].getCodFacultad() == codF:

                print(f"nombre: {self.__arreglo[i].getNombre()} |"
                      f"duracion: {self.__arreglo[i].getDuracion()}"
                    )

    def ordenar(self):
        self.__arreglo[:self.__cantidad].sort()