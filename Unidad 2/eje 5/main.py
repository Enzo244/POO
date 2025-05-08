from gestorBeca import gestorBeca
from gestorBeneficiario import gestorBene

def mostrar_menu():
    print("=== Menú de Opciones ===")
    print("a. Mostrar beneficiarios por tipo de beca e importe total")
    print("b. Verificar si un beneficiario tiene más de una beca")
    print("c. Listar beneficiarios ordenados de mayor a menor por Facultad")
    print("d. Listar estudiantes con promedio > 8 sin beca de ayuda económica")
    print("e. Salir")

if __name__ == "__main__":
    GB = gestorBeca()
    GB.cargar()
    GN = gestorBene()
    GN.cargar()
    #GB.mostrar()
    #GN.mostrar()

    opcion = ''
    while opcion != 'e':
        mostrar_menu()
        opcion = input("Ingrese una opción: ").lower()

        if opcion == 'a':
            tipoBeca=input("ingrese el tipo de beca: ")
            idBeca=GB.buscarBeca(tipoBeca)
            print(f"{idBeca}")
            importe= GB.getimportePorId(idBeca)
            print(f"{importe}")
            GN.informar(idBeca,importe)
        elif opcion == 'b':
            dni=input("ingrese un dni del beneficiario: ")
            idB=GN.buscarBeneficiario(dni)
            print(f"este es el id de beca del beneficiario: {idB}")
            GB.listarPorMasDeUnaBeca(idB)
        elif opcion == 'c':
            # Aquí va la funcionalidad de la opción c
            pass
        elif opcion == 'd':
            # Aquí va la funcionalidad de la opción d
            pass
        elif opcion == 'e':
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente nuevamente.")
