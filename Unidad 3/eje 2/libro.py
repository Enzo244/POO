class libro:
    __titulo: str
    __autor: str
    __isbn: str
    __genero: str

    def __init__(self,t,a,i,g):
        self.__titulo=t
        self.__autor=a
        self.__isbn=i
        self.__genero=g
    def __str__(self):
         return f"{self.__titulo} - {self.__autor} ({self.__genero})"
    
    def getTitulo(self):
        return self.__titulo
