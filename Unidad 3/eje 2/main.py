from gestorBiblio import gestorBiblio

def menu():
     print("=== Menu de opciones ===")
     print("a.agregar un libro a la biblioteca ")
     print("b. eliminar libro")
     print("c. mostrar datos de un libro")
     print("e. pa salir")

if __name__ == "__main__":
     GB= gestorBiblio()
     GB.cargar()

     opcion=""

     while opcion != "e":
          menu()
          opcion= input("ingrese una opcion: ")

          if opcion == "a":
               biblio= input("ingrese nombre de la biblioteca: ")
               GB.agregarUnLibro(biblio)
               GB.mostrar()
               
          elif opcion == "b":
               biblio= input("ingrese nombre de la biblioteca: ")
               b=GB.buscarBiblio(biblio)
               GB.eliminarLibro(b)

          elif opcion== "c":
               nombre= input("ingrese un titulo de un libro: ")
               GB.mostrarDatosPorTitulo(nombre)
          elif opcion == "e":
               print("SALIENDO DEL PROGRAMA")
          else:
               print("error")