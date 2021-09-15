from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Return import Return 

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
            nuevaTabla = TablaSimbolos(nTable)
            while valor2 >= valor1:
                for instruccion in self.instrucciones:
                    if isinstance(instruccion,Declaracion):
                        instruccion.local = True
                    result = instruccion.interpretar(tree,nuevaTabla)
                    if isinstance(result,Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result,Break): return result
                    if isinstance(result,Continue): 
                        valor1 = valor1 + 1
                        continue
                    if isinstance(result,Return): return result 
                valor1 = valor1 + 1
                simbolo = Simbolo(str(self.declaracion), self.expresionizq.tipo,self.arreglo,self.funcion, self.fila, self.columna, valor1)
                res = nuevaTabla.actualizarTabla(simbolo)
                if isinstance(res, Excepcion): return res
                if isinstance(result,Break): return result
                if isinstance(result,Continue): continue
                if isinstance(result,Return): return result  
        else:
            if self.expresioncad != None:
                cad = self.expresioncad.interpretar(tree,table)
                if isinstance(cad,Excepcion): return cad
                if self.expresioncad.tipo == TIPO.CADENA:
                    nTable = TablaSimbolos(table)
                    simbolo = Simbolo(str(self.declaracion), self.expresioncad.tipo,self.arreglo,self.funcion, self.fila, self.columna, "")
                    result = nTable.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result   
                    nuevaTabla = TablaSimbolos(nTable)
                    for cadena in cad:
                        simbolo = Simbolo(str(self.declaracion), self.expresioncad.tipo,self.arreglo,self.funcion, self.fila, self.columna, cadena)
                        res = nuevaTabla.actualizarTabla(simbolo)
                        for instruccion in self.instrucciones:
                            if isinstance(instruccion,Declaracion):
                                instruccion.local = True
                            result = instruccion.interpretar(tree,nuevaTabla)
                            if isinstance(result,Excepcion):
                                tree.getExcepciones().append(result)
                                tree.updateConsola(result.toString())
                            if isinstance(result,Break): return result
                            if isinstance(result,Continue): continue
                            if isinstance(result,Return): return result           