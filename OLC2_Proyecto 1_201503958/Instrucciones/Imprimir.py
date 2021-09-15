from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        cadena = ""
        for value in self.expresion:
            cadena += str(value.interpretar(tree,table))
            if isinstance(value.interpretar(tree,table),Excepcion):
                return value.interpretar(tree,table)

            if value.tipo == TIPO.ARREGLO:
                valores = value.interpretar(tree,table)
                for elemento in valores.get_list_value():
                    tree.updateConsola(elemento.valor)
                    return None

            if value.tipo == TIPO.NULO:
                return Excepcion("Semantico", "Null pointer, no se puede imprimir tipo NULL", self.fila, self.columna)
        tree.updateConsola(cadena)
        return None

        