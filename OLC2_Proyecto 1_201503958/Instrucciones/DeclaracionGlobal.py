from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion

class DeclaracionGlobal(Instruccion):
    def __init__(self, identificador, fila, columna,tipo,expresion = None):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.expresion = expresion
        self.arreglo = False
        self.variableGlobal = False

    def interpretar(self, tree, table):
        variable = tree.getGlobal(self.identificador)
        if variable!= None:
            self.variableGlobal = True
            if self.expresion!= None:
                variable.expresion.valor = self.expresion.interpretar(tree,table)
                table.actualizarGlobal(variable)
            return None
        else:
            return Excepcion("Semantico", "Variable global no existe",self.fila,self.columna)            