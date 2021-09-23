from typing import Dict
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Return import Return 
from Abstract.NodoAST import NodoAST


class For(Instruccion):
    def __init__(self,declaracion, expresionizq,expresionder,instrucciones,expresioncad,arr,fila, columna):
        self.declaracion = declaracion
        self.expresionizq = expresionizq
        self.expresionder = expresionder
        self.instrucciones = instrucciones
        self.expresioncad = expresioncad
        self.fila = fila
        self.arr = arr
        self.columna = columna
        self.arreglo = False
        self.funcion = False

    def interpretar(self, tree, table):
        if self.expresionizq != None and self.expresionder != None:
            valor1 = self.expresionizq.interpretar(tree,table)
            if isinstance(valor1,Excepcion): return valor1
            valor2 = self.expresionder.interpretar(tree,table)
            if isinstance(valor2,Excepcion): return valor2
            nTable = TablaSimbolos(table,"FOR")

            
            simbolo = Simbolo(str(self.declaracion), self.expresionizq.tipo,self.arreglo,self.funcion, self.fila, self.columna, valor1)
            result = nTable.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            nuevaTabla = TablaSimbolos(nTable,"FOR")
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
        elif self.expresioncad != None and not isinstance(self.expresioncad,Dict):
            if self.expresioncad != None:
                cad = self.expresioncad.interpretar(tree,table)
                if isinstance(cad,Excepcion): return cad
                if self.expresioncad.tipo == TIPO.CADENA:
                    nTable = TablaSimbolos(table,"FOR")
                    simbolo = Simbolo(str(self.declaracion), self.expresioncad.tipo,self.arreglo,self.funcion, self.fila, self.columna, "")
                    result = nTable.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result   
                    nuevaTabla = TablaSimbolos(nTable,"FOR")
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
                else:
                    nTable = TablaSimbolos(table,"FOR")
                    simbolo = Simbolo(str(self.declaracion), cad[0].tipo,self.arreglo,self.funcion, self.fila, self.columna, cad[0].valor)
                    result = nTable.setTabla(simbolo)
                    for instr in cad:
                        x = instr.interpretar(tree,nTable)
                        simbolo = Simbolo(str(self.declaracion), x.tipo,self.arreglo,self.funcion, self.fila, self.columna, x.valor)
                        res = nTable.actualizarTabla(simbolo)
                        res = instr.interpretar(tree,nTable)
                        if isinstance(res,Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(res,Break): return result
                        if isinstance(res,Continue): continue
                        if isinstance(res,Return): return result
        elif self.arr != None:
            valores = self.arr['valores']
            arra = []
            for x in valores:
                z = x.interpretar(tree,table)
                sim = Simbolo("",x.tipo,False,False,self.fila,self.columna,z)
                arra.append(sim)
            sim = Simbolo(str(self.declaracion),self.arr['tipo'],False,False,self.fila,self.columna,arra)
            tablita=TablaSimbolos(table,"FOR")
            verifi = tablita.setTabla(sim)
            if isinstance(verifi,Excepcion):return verifi
            Ntab=TablaSimbolos(tablita,"FOR")
            for carac in arra:
                sim = Simbolo(str(self.declaracion),carac.tipo,False,False,self.fila,self.columna,carac.getValor())
                res = Ntab.actualizarTabla(sim)
                if isinstance(res,Excepcion):res
                for inst in self.instrucciones:
                    resul = inst.interpretar(tree,Ntab)
                    if isinstance(resul,Excepcion):
                        tree.getExcepciones().append(resul)
                        tree.updateConsola(resul.toString())



    def getNodo(self):
        nodo = NodoAST("FOR")

        Instrucciones = NodoAST("INSTRUCCIONES FOR")
        for instr in self.instrucciones:
            Instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(Instrucciones)
        return nodo