import csv
from tramo import tramo

class gestorTramo:
    __listaTramo: list
    def __init__(self):
        self.__listaTramo=[]
    
    def cargar(self):
        
        with open("tramos.csv",'r',encoding="utf-8") as archivoTramo:
            reader=csv.reader(archivoTramo, delimiter=";")
            next(reader)
            for tram in reader:
                unTramo= tramo(tram[0],tram[1],tram[2],tram[3])
                self.agregar(unTramo)
                print(f"patente: {unTramo.getPatente()}")
    
    def agregar(self,unTramo):
        self.__listaTramo.append(unTramo)

    def mostrarDatosPorPatente(self, patente):
        total_km = 0
        for tramo in self.__listaTramo:
            if tramo.getPatente() == patente:
                print(f"Ciudad de origen: {tramo.getCiudadOrigen()}")
                print(f"Ciudad destino: {tramo.getCiudadDestino()}")
                print(f"Kilómetros recorridos: {tramo.getDistancia()} km\n")
                total_km += tramo.getDistancia()
        
        print(f"Total de kilómetros recorridos por la patente {patente}: {total_km} km")

    def calcularDistancia(self,patente, consumoP):
        cantKm=0
        for tra in self.__listaTramo:
            if patente == tra.getPatente():
                cantKm+= tra.getDistancia()
        gasto= (cantKm * consumoP)/ 100

        print(f"Patente: {patente}")
        print(f"  Kilómetros recorridos: {cantKm} km")
        print(f"  Gasto estimado de combustible: {gasto:.2f} litros\n")


    def listarPorDistancia(self,distancia):
        
        print(f"\nTramos con distancia menores a {distancia} km:\n")

        for tra in self.__listaTramo:
            if tra > float(distancia):
                print(f"ciudad origen : {tra.getCiudadOrigen()}")
                print(f"ciudad destino: {tra.getCiudadDestino()}")
                print(f"patente:  {tra.getPatente()}")
                print(f"distancia: {tra.getDistancia()}\n")