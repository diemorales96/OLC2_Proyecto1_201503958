from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos

class Break(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self