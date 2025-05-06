from gestorPaciente import gestorPaciente
from gestorAtencion import gestorAtencion
if __name__== "__main__":
    GP= gestorPaciente()
    GP.cargar()
    #GP.mostrar()
    GA=gestorAtencion()
    GA.cargar()
    GA.mostrar()