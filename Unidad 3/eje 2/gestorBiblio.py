import csv
from biblio import biblioteca
from libro import libro
class gestorBiblio:
    __lista: list

    def __init__(self):
        self.__lista= []

    def cargar(self):
        i= -1
        with open(r"C:\Users\Enzo\Desktop\POO\Unidad 3\eje 2\Biblioteca.csv", 'r', encoding="utf-8") as archivoBiblio:
            reader= csv.reader(archivoBiblio, delimiter=";")

            for fila in reader:
                if len(fila) ==3:
                    unaBiblio= biblioteca(fila[0],fila[1],fila[2],)
                    self.agregarBiblio(unaBiblio)
                    i+=1
                else:
                    unLibro= libro(fila[0],fila[1],fila[2],fila[3])
                    self.__lista[i].agregarLibro(unLibro)
                    

    def agregarBiblio(self,unaBiblio):
        self.__lista.append(unaBiblio)
    
    def mostrar(self):
        for biblio in self.__lista:
            print("=" * 50)
            print(f"{biblio}")
            biblio.mostrarLibros()
            print()  # 