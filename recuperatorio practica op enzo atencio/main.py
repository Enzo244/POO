from gestorMedicos import gestorMedico
from gestorVisitas import gestorVisitas

def mostrar_menu():
    print("=== Menú de Opciones ===")
    print("a. ingrese dni y emitir listado de las visitas")
    print("b. mostrar datos de todos los medicos")
    print("c. listar visitas realizadas en una zona")
    print("e. Salir")

if __name__=="__main__":
    cantidad=int(input("ingrese la cantidad de medicos: "))
    GM=gestorMedico(cantidad)
    GM.cargar()
    GV=gestorVisitas()
    GV.cargar()

    opcion = ''
    while opcion != 'e':
        mostrar_menu()
        opcion = input("Ingrese una opción: ").lower()

        if opcion == 'a':
            dni=input("ingrese dni: ")
            GV.mostrarListado(dni)

        elif opcion == 'b':
            GM.mostrarPorCadaMedico(GV)
            
        elif opcion == 'c':
            zona=input("ingrese una zona: ")
            GV.listarPorZona(GM,zona)
        elif opcion == 'e':
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")