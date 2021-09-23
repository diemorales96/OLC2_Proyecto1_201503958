from Abstract.Instruccion import Instruccion
from Expresiones.Identificador import Identificador
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST

class Imprimir2(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        cadena = ""
        for value in self.expresion:
            val = value.interpretar(tree,table)
            if value.tipo == TIPO.ARREGLO and isinstance(value,Identificador):
                arr = table.getTabla(value.identificador)
                cadena += arr.arraysito(val,tree,table)
            else:
                if isinstance(val,Simbolo):
                    if val.tipo != TIPO.ARREGLO:
                        cadena+= str(val.getValor())
                    else:
                        cadena+=val.arraysito(val.getValor(),tree,table)
                else:
                    cadena += str(val)
            if isinstance(value.interpretar(tree,table),Excepcion): return val

            if value.tipo == TIPO.NULO:
                return Excepcion("Semantico", "Null pointer, no se puede imprimir tipo NULL", self.fila, self.columna)
        tree.updateConsola(cadena)
        return None

    def getNodo(self):
        nodo = NodoAST("IMPRIMIR")
        for exp in self.expresion:
            nodo.agregarHijoNodo(exp.getNodo())
        return nodo