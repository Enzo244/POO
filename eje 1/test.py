from targetaSube import targetaSube
from controladorTargetas import contenedorTargetas

def test():
    CT = contenedorTargetas()  # <- crear instancia

    for i in range(3):    
        saldo= int(input("ingrese saldo:"))
        numSube= input("ingrese numero de targeta:")
        CT.cargar(saldo,numSube)
    #CT.mostrar()

    CT.saldoNegativo()

    CT.obtenerSaldo()