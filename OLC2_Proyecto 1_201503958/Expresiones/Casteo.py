from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST


class Casteo(Instruccion):
    def __init__(self, tipo,expresion, fila, columna):
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        val = self.expresion.interpretar(table,tree)

        if self.tipo == TIPO.CADENA:
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                   return  str(self.obtenerVal(self.expresion.tipo,val))
                except:
                    return Excepcion("Semantico","Nose puede Parsear para String.",self.fila,self.columna)
            elif self.expresion.tipo == TIPO.ENTERO:
                try:
                   return  str(self.obtenerVal(self.expresion.tipo,val))
                except:
                    return Excepcion("Semantico","Nose puede Parsear para String.",self.fila,self.columna)
            return Excepcion("Semantico","Tipo erroneo de parseo para String.")
        if self.tipo == TIPO.DECIMAL:
            if self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede parseo para Float64.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de parseo para Float64.", self.fila, self.columna)        
        if self.tipo == TIPO.ENTERO:
            if self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede parseo para Int64.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de parseo para Int64.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(self.tipo)
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
            