from hotel import hotel
import csv
class gestorHotel:
    __lista: list
    def __init__(self):
        self.__lista= []
    
    def cargar(self):
        with open("C:\Users\Enzo\Desktop\POO\Unidad 3\eje 1\Hoteles.csv", 'r', encoding='UTF-8') as archivoHoteles:
            reader = csv.reader(archivoHoteles, delimiter=";")
            next(reader)
            for fila in reader:
                if type(fila[0]) == str:
                    unhotel = hotel(fila[0],fila[1],fila[2],fila[3])
                    self.agregarHotel(unhotel)
                else:
                    unhotel.agregar(fila[0],fila[1],fila[2],fila[3],fila[4])
                    print("Carreras cargadas:")
            for hotel in self.__lista:
                print(f"- {hotel.getNombre()}")

    def agregarHotel(self,unHotel):

        self.__lista.append(unHotel)
