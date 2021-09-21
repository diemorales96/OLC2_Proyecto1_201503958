
class Simbolo:
    def __init__(self, identificador, tipo, arreglo,funcion, fila, columna, valor,parametro = False ):
        self.id = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.arreglo = arreglo
        self.funcion = funcion
        self.parametro = parametro

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo  

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def getArreglo(self):
        return self.arreglo

    def getFuncion(self):
        return self.funcion