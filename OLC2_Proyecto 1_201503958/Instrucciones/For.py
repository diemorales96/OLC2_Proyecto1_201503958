from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

class For(Instruccion):
    def __init__(self,declaracion, expresionizq,expresionder,instrucciones,expresioncad,fila, columna):
        self.declaracion = declaracion
        self.expresionizq = expresionizq
        self.expresionder = expresionder
        self.instrucciones = instrucciones
        self.expresioncad = expresioncad
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        self.funcion = False

    def interpretar(self, tree, table):
        if self.expresionizq != None and self.expresionder != None:
            valor1 = self.expresionizq.interpretar(tree,table)
            if isinstance(valor1,Excepcion): return valor1
            valor2 = self.expresionder.interpretar(tree,table)
            if isinstance(valor2,Excepcion): return valor2
            nTable = TablaSimbolos(table)

            
            simbolo = Simbolo(str(self.declaracion), self.expresionizq.tipo,self.arreglo,self.funcion, self.fila, self.columna, valor1)
            result = nTable.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            if isinstance(result, Break): return result
            while valor2 >= valor1:
                nuevaTabla = TablaSimbolos(nTable)
                for instruccion in self.instrucciones:
                    result = instruccion.interpretar(tree,nuevaTabla)
                    if isinstance(result,Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result,Break): return result
                valor1 = valor1 + 1
                simbolo = Simbolo(str(self.declaracion), self.expresionizq.tipo,self.arreglo,self.funcion, self.fila, self.columna, valor1)
                res = nuevaTabla.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                if isinstance(result,Break): return result
        else:
            if self.expresioncad != None:
                cad = self.expresioncad.interpretar(tree,table)
                if isinstance(cad,Excepcion): return cad
                if self.expresioncad.tipo == TIPO.CADENA:
                    nTable = TablaSimbolos(table)
                    simbolo = Simbolo(str(self.declaracion), self.expresioncad.tipo,self.arreglo,self.funcion, self.fila, self.columna, "")
                    result = nTable.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result,Break): return result    
                    for cadena in cad:
                        nuevaTabla = TablaSimbolos(nTable)
                        simbolo = Simbolo(str(self.declaracion), self.expresioncad.tipo,self.arreglo,self.funcion, self.fila, self.columna, cadena)
                        res = nuevaTabla.actualizarTabla(simbolo)
                        for instruccion in self.instrucciones:
                            result = instruccion.interpretar(tree,nuevaTabla)
                            if isinstance(result,Excepcion):
                                tree.getExcepciones().append(result)
                                tree.updateConsola(result.toString())
                            if isinstance(result,Break): return result         