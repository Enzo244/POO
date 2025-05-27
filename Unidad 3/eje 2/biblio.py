class biblioteca:
    __nombre: str
    __dirreccion: str
    __telefono: str
    __listaLibros: list

    def __init__(self,n,d,t):
        self.__nombre=n
        self.__dirreccion=d
        self.__telefono=t
        self.__listaLibros= []

    def __str__(self):
        return f"Nombre: {self.__nombre}\nDirección: {self.__dirreccion}\nTeléfono: {self.__telefono}\nCantidad de libros: {len(self.__listaLibros)}\n"

    def getNombre(self):
        return self.__nombre
    
    def agregarLibro(self,unLibro):
        self.__listaLibros.append(unLibro)

    def mostrarLibros(self):
        if not self.__listaLibros:
            print("  No hay libros disponibles.")
        else:
            print("\n  Libros:")
            for i, libro in enumerate(self.__listaLibros, start=1):
                print(f"    {i}. {libro}")
    
    def eliminarLibroPorTitulo(self,li):

        for l in self.__listaLibros:
            if li == l.getTitulo():
                self.__listaLibros.remove(l)
                return True
        return False
                