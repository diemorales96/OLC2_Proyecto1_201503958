
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos


class DeclaracionLocal(Instruccion):
    def __init__(self,identificador,fila,columna,tipo,expresion=None):
        self.identificador=identificador
        self.tipo=tipo
        self.expresion=expresion
        self.fila=fila
        self.columna=columna
        self.arreglo=False
        self.funcion = False


    def interpretar(self, tree, table):


     if self.expresion == None:
         value = None
         if isinstance(value, Excepcion): return value
         simbolo = Simbolo(str(self.identificador), TIPO.NULO, self.arreglo,self.funcion, self.fila, self.columna, None)
         result = table.setTabla(simbolo)
         if isinstance(result, Excepcion): 
             res = table.actualizarTabla(simbolo)
             if isinstance(res, Excepcion): return res
         return None
     else:
        value = self.expresion.interpretar(tree, table)  
        if isinstance(value, Excepcion): return value
        simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.arreglo,self.funcion, self.fila, self.columna, value)
        result = table.setTabla(simbolo)
        #tree.setSimbolo(simbolo)
        if isinstance(result, Excepcion): 
            res = table.actualizarTabla(simbolo)
            if isinstance(res,Excepcion): return res
        return None


