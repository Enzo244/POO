import csv
from beca import beca
class gestorBeca:
    __listaBeca: list
    def __init__(self):
        self.__listaBeca= []

    def  cargar(self):
        with open("eje 5/becas.csv", 'r', encoding="utf-8" ) as archivoBecas:
            reader= csv.reader(archivoBecas, delimiter=";")
            next(reader)
            for bec in reader:
                unaBeca= beca(int(bec[0]), bec[1], float(bec[2]))
                self.agregar(unaBeca)
    
    def agregar(self,unaBeca):

        self.__listaBeca.append(unaBeca)

    def mostrar(self):
        for beca in self.__listaBeca:
            print (beca)

    def buscarBeca(self,tipoB):
        i=0
        while i< len(self.__listaBeca) and tipoB != self.__listaBeca[i].getTipoBeca():
            i+=1
        if i < len(self.__listaBeca):
            return self.__listaBeca[i].getIdBeca()
    
    def getimportePorId(self, idB):
        
        for beca in self.__listaBeca :
            if idB== beca.getIdBeca():
                return beca.getImporte()
            
    def listarPorMasDeUnaBeca(self,idB):
        for beca in self.__listaBeca:
            if idB== self.__listaBeca.getIdBeca():
                if idB== self.__listaBeca.getIdBeca():
                    print(f"esta persona tiene mas de 1 beca asociada: {beca.getTipoBeca()}")