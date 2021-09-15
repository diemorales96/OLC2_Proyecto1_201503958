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
        self.local = None


    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value
        
        if self.tipodec != None:
            if self.tipodec != self.expresion.tipo:
                return Excepcion("Semantico", "No coinciden los tipos",self.fila,self.columna)
            else:
                simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
                result = table.setTabla(simbolo)
                if isinstance(result, Excepcion): 
                    resultado = table.actualizarTabla(simbolo)
                    if isinstance(resultado,Excepcion):return resultado
        else:
            if self.local == True:
                simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
                if table.getTablasLocales(simbolo.id) != None:
                    res = table.actualizarTabla(simbolo)
                    if isinstance(res,Excepcion): return res
                    return None
                simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
                res = table.setTabla(simbolo)
                if isinstance(res,Excepcion): return res
                return None
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo,self.funcion, self.fila, self.columna, value)
            if table.getTabla(simbolo.id) != None:
                result = table.actualizarTabla(simbolo)
                if isinstance(result,Excepcion):return result    
            else:
                result = table.setTabla(simbolo)
                if isinstance(result,Excepcion): return result
            return None