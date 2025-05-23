from gestorTramo import gestorTramo
from gestorColectivo import gestorColectivo

def mostrar_menu():
    print("=== Menú de Opciones ===")
    print("a. Mostrar datos de un chofer por su dni")
    print("b. Mostrar km recorridos y gastos por cada colectivo")
    print("c. listar datos dada una distancia")
    print("e. Salir")

if __name__=="__main__":

    GT=gestorTramo()
    GT.cargar()
    GC=gestorColectivo()
    GC.cargar()

    opcion = ''
    while opcion != 'e':
        mostrar_menu()
        opcion = input("Ingrese una opción: ").lower()

        if opcion == 'a':
            dni=input("ingrese el dni del chofer: ")
            patenteDelChofer=GC.buscarChofer(dni)
            if patenteDelChofer is not None:
                print(patenteDelChofer)
                GT.mostrarDatosPorPatente(patenteDelChofer)
            else:
                print("patente no encontrada")

        elif opcion == 'b':
            GC.recorrerColectivos(GT)
            
        elif opcion == 'c':
            distanciaRecorrida=input("ingrese distancia recorrida: ")
            GT.listarPorDistancia(distanciaRecorrida)
        elif opcion == 'e':
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")
