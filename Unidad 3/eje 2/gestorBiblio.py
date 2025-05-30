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
            print()   

    def buscarBiblio(self,biblio):
        i=0
        while i< len(self.__lista) and biblio != self.__lista[i].getNombre():
            i+=1
        if i < len(self.__lista):
            unaBiblio= self.__lista[i]

        return unaBiblio

    def agregarUnLibro(self,biblio):
            unaBiblio= self.buscarBiblio(biblio)
            if unaBiblio:
                a=input("ingrese Título: ")
                b=input("ingrese Autor: ")
                c=input("ingrese ISBN: ")
                d=input("ingrese Género: ")
                unLibro= libro(a,b,c,d)

                unaBiblio.agregarLibro(unLibro)
                print(f"\n✅ Libro '{a}' agregado a la biblioteca '{biblio}'.\n")
            else:
                print(f"\n❌ Biblioteca '{biblio}' no encontrada.\n")

    def eliminarLibro(self,biblio):
        if biblio:
    
            libro=input("ingrese libro a eliminar: ")
            bandera=biblio.eliminarLibroPorTitulo(libro)

            if bandera :
                print(f"\nLibro '{libro}' eliminado de la biblioteca '{biblio.getNombre()}'.\n")
            else:
                print(f"\nLibro '{libro}' no encontrado en la biblioteca\n '{biblio.getNombre()}'.\n")

    def mostrarDatosPorTitulo(self,titulo):
        
        for biblio in self.__lista:
            if biblio.buscarPorTitulo(titulo):
                print(f"\nla biblioteca '{biblio.getNombre()}'.\n")
            else:
                print("no se encontro")
