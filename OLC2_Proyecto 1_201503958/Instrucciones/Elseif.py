from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodoAST import NodoAST
class Elseif(Instruccion):
    def __init__(self,condicion,instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna


    def interpretar(self, tree, table):
        condicion=self.condicion.interpretar(tree,table)
        if isinstance(condicion,Excepcion): return condicion

    def getInstrucciones(self):
        return self.instrucciones

    def getNodo(self):
        nodo = NodoAST("ELSEIF")

        instruccionesIf = NodoAST("INSTRUCCIONES ElSEIF")
        for instr in self.instrucciones:
            instruccionesIf.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instruccionesIf)
        return nodo