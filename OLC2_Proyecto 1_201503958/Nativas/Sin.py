from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
import math

class Sin(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("sin##param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de sin", self.fila, self.columna)

        if simbolo.tipo != TIPO.DECIMAL: 
            if simbolo.tipo != TIPO.ENTERO:
                return Excepcion("Semantico", "Tipo de parametro de sin no es numero.", self.fila, self.columna)

        self.tipo = simbolo.tipo
        return math.sin(simbolo.getValor())