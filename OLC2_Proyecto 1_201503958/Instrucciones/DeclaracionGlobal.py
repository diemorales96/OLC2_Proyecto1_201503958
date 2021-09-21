from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST


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
                variable.expresion.tipo = self.expresion.tipo
                table.actualizarGlobal(variable)
            return None
        else:
            return Excepcion("Semantico", "Variable global no existe",self.fila,self.columna)            

    def getNodo(self):
        nodo = NodoAST("DECLARACION GLOBAL")
        if self.expresion!=None:
            nodo.agregarHijo(str(self.identificador))
            nodo.agregarHijoNodo(self.expresion.getNodo())
        else:
            nodo.agregarHijo(str(self.identificador))
        return nodo