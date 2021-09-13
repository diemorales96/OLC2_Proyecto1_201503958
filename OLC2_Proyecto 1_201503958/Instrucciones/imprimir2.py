from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Imprimir2(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table)  

        if isinstance(value, Excepcion) :
            return value

        if self.expresion.tipo == TIPO.ARREGLO:
            return Excepcion("Semantico", "No se puede imprimir un arreglo completo", self.fila, self.columna)
        elif self.expresion.tipo == TIPO.NULO:
            return Excepcion("Semantico", "Null pointer, no se puede imprimir tipo NULL", self.fila, self.columna)
        tree.updateConsola2(value)
        return None