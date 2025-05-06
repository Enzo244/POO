import csv
from beneficiario import beneficiario
class gestorBene:
    __listaBeneficiario: list

    def __init__(self):
        self.__listaBeneficiario=[]

    def cargar(self):
        with open("eje 5/beneficiarios.csv" ,'r', encoding="utf-8") as archivoBeneficiario:
            reader= csv.reader(archivoBeneficiario , delimiter=";")
            next(reader)
            for ben in reader:
                unBeneficiario=beneficiario((ben[0]),ben[1],ben[2],ben[3],ben[4],ben[5],(ben[6]),(ben[7]))
                self.agregar(unBeneficiario)
                    
    def agregar(self,unBene):
        self.__listaBeneficiario.append(unBene)

    def mostrar(self):
        for ben in self.__listaBeneficiario:
            print(ben)
        
    def informar(self,idBeca,importe):
        print(f"Beneficiarios con la beca ID {idBeca}:")
        cont=0
        for beneficiario in self.__listaBeneficiario:
            if int(beneficiario.getIdBeca()) == int(idBeca):
                print(f"- {beneficiario.getNombre()}")
                cont+=1
        print(f"personas: {cont}")
        print(f"importe: {importe}")
        print(f"importe total que debe disponer la Secretaría para el pago de dicha Beca es: {cont*importe}")

    def buscarBeneficiario(self,dni):
        i=0
        while i< len(self.__listaBeneficiario) and self.__listaBeneficiario[i].getDni() != dni :
            i+=1
        if i< len(self.__listaBeneficiario):
            return self.__listaBeneficiario[i].getIdBeca()