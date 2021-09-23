from TS.Tipo import TIPO


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


    def arraysito(self,array,tree,table):
        cadenita="["
        contador=0
        if isinstance(array,Simbolo):
            array=array.getValor()
        for x in array:
            contador=contador+1
            if x.tipo!=TIPO.ARREGLO:
                cadenita+=str(x.getValor())
                if contador<len(array):
                    cadenita+=","
            else:
                
                cadenita+=self.arraysito(x,tree,table)
                
                if contador<len(array):
                    cadenita+=","
            
        cadenita+="]"
        return cadenita