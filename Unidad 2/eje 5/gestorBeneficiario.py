import csv
from beneficiario import beneficiario
class gestorBene:
    __listaBeneficiario: list

    def __init__(self):
        self.__listaBeneficiario=[]

    def cargar(self):
        with open("Unidad 2/eje 5/beneficiarios.csv" ,'r', encoding="utf-8") as archivoBeneficiario:
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

    def contarIdBecas(self,dni):
        cont=0
        for ben in self.__listaBeneficiario:
            
            if ben.getDni() == dni:
                Nom= ben.getNombre()
                app= ben.getApellido()
                cont+=1
        if cont == 1:
            print("el benficiario tiene solo una beca")
        elif cont > 1:
            print(f"el beneficiario {Nom} {app} tiene mas de una beca")
        else:
            "no se encontro"
            