import csv
from paciente import Paciente

class gestorPaciente:
    __listaPaciente: list
    def __init__(self):
        self.__listaPaciente= []
    
    def cargar(self):

        with open("pacientes.csv",'r', encoding="utf-8") as archivoPaciente:
            reader= csv.reader(archivoPaciente, delimiter=";")
            next(reader)
            for pac in reader:
                unP= Paciente(pac[0],pac[1],(pac[2]))
                self.agregar(unP)
    
    def agregar(self,unaP):
        self.__listaPaciente.append(unaP)
    
    def mostrar(self):
        for pac in self.__listaPaciente:
            print (pac)