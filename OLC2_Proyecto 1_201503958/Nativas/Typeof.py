from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion


class Typeof(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeof##param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Typeof", self.fila, self.columna)
        self.tipo = simbolo.tipo
        p = self.obtenerTipo(self.tipo)
        return p
    
    def obtenerTipo(self,tipo):
        if tipo == TIPO.NULO:
            return "> NULO"
        elif tipo == TIPO.ENTERO:
            return "> INT64"
        elif tipo == TIPO.DECIMAL:
            return "> FLOAT64"
        elif tipo == TIPO.BOOLEANO:
            return "> BOOL"
        elif tipo == TIPO.CADENA:
            return "> STRING"
        elif tipo == TIPO.CHARACTER:
            return "> CHAR"
        elif tipo == TIPO.ARREGLO:
            return "> ARRAY"
        else:
            return Excepcion("Semantico", "No se encontró el tipo para Typeof", self.fila, self.columna) 