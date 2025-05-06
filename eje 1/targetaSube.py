class targetaSube:
    __saldo: int
    __numero: int
    def __init__(self,saldo,numero):
        self.__saldo= saldo
        self.__numero= numero
    
    def getSaldo(self):
        return self.__saldo
    def getNumero(self):
        return self.__numero
    
    def cargarSaldo(self,importe):
        if self.__saldo > 0:
            self.__saldo += importe
    def __str__(self):
        return f"Saldo: {self.__saldo} numero de targeta: {self.__numero}"
    
    def pagarPasaje(self,importe):

        if self.__saldo > importe: 
            self.__saldo - importe 
            print("su nuevo saldo es de:",self.__saldo)
        else:
            return print("tu saldo no es suficiente")
        
    def consultarSaldo(self):
        return print("su saldo es de ", self.__saldo)
    
