from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
import math

class Truncate(Instruccion):
    def __init__(self,expresion, fila, columna):
        self.expresion = expresion
        self.tipo = TIPO.ENTERO
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree,table)
        if isinstance(value,Excepcion):return value
        if self.expresion.tipo == TIPO.DECIMAL:
            return math.trunc(value)

    def getNodo(self):
        nodo = NodoAST("TRUNC")
        return nodo