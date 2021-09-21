from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST


class If(Instruccion):
    def __init__(self, condicion,instruccionIf,instruccionesElse,instruccioneselseif, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionIf
        self.instruccionesElse = instruccionesElse
        self.instruccionesElseif = instruccioneselseif
        self.fila = fila
        self.columna = columna
        self.local = None

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree,table)
        if isinstance(condicion,Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOLEANO:
            if bool(condicion) == True:
                nuevaTabla = TablaSimbolos(table,"IF")
                for instruccion in self.instruccionesIf:
                    if isinstance(instruccion,Declaracion):
                        instruccion.local = True   
                    result = instruccion.interpretar(tree,nuevaTabla)
                        
                    if isinstance(result,Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result,Break): return result
                    if isinstance(result,Continue): return result
                    if isinstance(result,Return): return result
                    
            else:
                if self.instruccionesElseif != None:
                    for instruccion in self.instruccionesElseif:
                        condicion = instruccion.condicion.interpretar(tree,table)
                        if condicion ==  True:
                            for instrElseif in instruccion.getInstrucciones():
                                
                                if isinstance(instruccion,Declaracion):
                                    instruccion.local = True
                                result = instrElseif.interpretar(tree,table)
                                if isinstance(result,Excepcion):
                                    tree.getExcepciones().append(result)
                                    tree.updateConsola(result.toString())
                                if isinstance(result,Break): return result
                                if isinstance(result,Continue): return result
                                if isinstance(result,Return): return result
                                  
                    if self.instruccionesElse != None and condicion == False:
                        for instr in self.instruccionesElse:
                            if isinstance(instr,Declaracion):
                                instr.local = True
                            result = instr.interpretar(tree,table)
                            if isinstance(result,Excepcion): return result
                            if isinstance(result,Break): return result
                            if isinstance(result,Continue): return result
                            if isinstance(result,Return): return result
                                  
                elif self.instruccionesElse != None:
                    for instr in self.instruccionesElse:
                        if isinstance(instr,Declaracion):
                            instr.local = True
                        result = instr.interpretar(tree,table)
                        if isinstance(result,Excepcion): return result
                        if isinstance(result,Break): return result
                        if isinstance(result,Continue): return result
                        if isinstance(result,Return): return result 
                               
        else:   
           return Excepcion("Semantico","Tipo d e dato no booleano en If.",self.fila,self.columna) 

    def getNodo(self):
        nodo = NodoAST("IF")

        instruccionesIf = NodoAST("INSTRUCCIONES IF")
        for instr in self.instruccionesIf:
            instruccionesIf.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instruccionesIf)

        if self.instruccionesElse != None:
            instruccionesElse = NodoAST("INSTRUCCIONES ELSE")
            for instr in self.instruccionesElse:
                instruccionesElse.agregarHijoNodo(instr.getNodo())
            nodo.agregarHijoNodo(instruccionesElse) 
        elif self.instruccionesElseif != None:
            for intr in self.instruccionesElseif:
                nodo.agregarHijoNodo(intr.getNodo())

        return nodo  