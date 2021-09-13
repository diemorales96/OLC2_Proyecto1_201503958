from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo

class Declaracion(Instruccion):
    def __init__(self, identificador, fila, columna, expresion,tipodec):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        self.funcion = False
        self.tipodec = tipodec
       


    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value
        if self.tipodec == self.expresion.tipo:
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
        elif self.tipodec == None:
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
            resultado = table.actualizarTabla(simbolo)
            if isinstance(resultado,Excepcion):
                result = table.setTabla(simbolo)
                if isinstance(result, Excepcion): return result
        else:
            return Excepcion("Semantico", "Tipos no coinciden.", self.fila, self.columna)
        return None
        