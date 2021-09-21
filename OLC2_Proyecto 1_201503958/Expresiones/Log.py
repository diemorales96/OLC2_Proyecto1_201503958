from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
import math

class Log(Instruccion):
    def __init__(self,expresion1,expresion2, fila, columna):
        self.expresion1 = expresion1
        self.expresion2 = expresion2
        self.tipo = TIPO.ENTERO
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value1 = self.expresion1.interpretar(tree,table)
        if isinstance(value1,Excepcion): return value1
        value2 = self.expresion2.interpretar(tree,table)
        if isinstance(value2,Excepcion): return value2

        if self.expresion1.tipo == TIPO.ENTERO:
            if self.expresion2.tipo == TIPO.ENTERO or self.expresion2.tipo == TIPO.DECIMAL:
                return math.log(value2,value1)
            else:
                return Excepcion("Semantico","No se puede obtener el valor del logaritmo de este tipo de dato.",self.fila,self.columna)
        else:
            return Excepcion("Semantico","No se puede obtener el valor del logaritmo con este tipo en la base.",self.fila,self.columna)

    def getNodo(self):
        nodo = NodoAST("LOG")
        return nodo