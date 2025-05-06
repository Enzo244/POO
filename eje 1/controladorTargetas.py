from targetaSube import targetaSube
class contenedorTargetas:
    __lista: list
    def __init__(self):
        self.__lista= []
    
    def cargar(self,saldo,numSube):
        unaTargeta= targetaSube(saldo,numSube)
        self.__lista.append(unaTargeta)

    def agregarTargeta(self,unaTargeta):
        self.__lista.append(unaTargeta)

    def mostrar(self):
        for unaSube in self.__lista:
            print (unaSube)

    def saldoNegativo(self):
        for unaSube in self.__lista:
            if unaSube.getSaldo() < 0:
                print ("estas targetas tienen saldo negativo",unaSube)
    def obtenerSaldo(self):
        numTargeta=input("ingrese numero de targeta")
        i=0
        encontrado= False
        while self.__lista[i].getNumero() == numTargeta and encontrado== True:
            print("el saldo de su sube es:",self.__lista[i].getSaldo())