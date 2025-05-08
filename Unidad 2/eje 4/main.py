from manejadorCarrera import manejadorCarrera
from manejadorfacultad import manejadorFacultad


if __name__ == '__main__':
    MC= manejadorCarrera()
    MF=manejadorFacultad()
    MF.cargar()
    MC.cargar()
    MC.ordenar()
    opcion = 10
    while opcion != 0:
        print("\n MENU DE OPCIONES \n")
        print("1.Buscar facultad.")
        print("2.Mostrar cantidad de carreras por facultad.")
        print("3.Mostrar carreras.")
        print("4.Salir.")
        opcion = int(input("Ingrese el número de la opción que desea: "))
        if opcion == 1:
            nombre= input("Ingrese nombre de la carrera: ")
            MC.BuscarCarrera(nombre,MF)

        elif opcion == 2:
            MF.contarCarreras(MC)

        elif opcion == 3:
            nomFacu=input("ingrese el nombre de la facultad: ")
            MF.listarCarreras(nomFacu,MC)

        elif opcion == 4:
            opcion= 0