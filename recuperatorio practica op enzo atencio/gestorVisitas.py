import csv
from visita import Visita
class gestorVisitas:
    __lista: list

    def __init__(self):
        self.__lista= []
    
    def cargar(self):
        with open("visitas.csv", 'r', encoding='UTF-8') as archivoVisitas:
            reader = csv.reader(archivoVisitas, delimiter=";")
            next(reader)  
            for visi in reader:
                unaVisita = Visita(visi[0],visi[1],visi[2],visi[3],visi[4],)

                self.agregar(unaVisita)
        print("Visitas cargadas")

        for visita in self.__lista:
            print(f"- {visita.getFecha()}")

    def agregar(self,unaVisita):
        self.__lista.append(unaVisita)

    def mostrarListado(self, dni):
        cont = 0
        for visi in self.__lista:
            if dni == visi.getDniMedico(): 
                print(f"Fecha: {visi.getFecha()}")
                print(f"Zona: {visi.getZona()}")
                print(f"Diagnóstico: {visi.getDiagnostico()}\n")
                cont += 1
        print(f"Se atendió un total de {cont} veces.")

    def totalVisitasRealizadas(self,dniM,valorF):
        cont=0
        for visi in self.__lista:
            if dniM == visi.getDniMedico():
                cont+=1
        print(f"total de visitas: {cont}")
        importeT= cont*valorF
        print(f"importe total a facturar: {importeT}\n")

    def listarPorZona(self,GM,zona):

        for visi in self.__lista:
            if visi == zona:
                print(f"Fecha: {visi.getFecha()}")
                print(f"DNI Del paciente: {visi.getDniPaciente()}")
                GM.mostrarNombrePorDni(visi.getDniMedico())
                print(f"Diagnóstico: {visi.getDiagnostico()}\n")
                

