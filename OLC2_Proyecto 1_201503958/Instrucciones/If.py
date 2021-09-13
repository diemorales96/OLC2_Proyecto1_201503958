from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class If(Instruccion):
    def __init__(self, condicion,instruccionIf,instruccionesElse,instruccioneselseif, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionIf
        self.instruccionesElse = instruccionesElse
        self.instruccionesElseif = instruccioneselseif
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree,table)
        if isinstance(condicion,Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOLEANO:
            if bool(condicion) == True:
                nuevaTabla = TablaSimbolos(table)
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree,nuevaTabla)
                    if isinstance(result,Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result,Break): return result
            else:
                if self.instruccionesElseif != None:
                    for instruccion in self.instruccionesElseif:
                        condicion = instruccion.condicion.interpretar(tree,table)
                        if condicion ==  True:
                            for instrElseif in instruccion.getInstrucciones():
                                result = instrElseif.interpretar(tree,table)
                                if isinstance(result,Excepcion):
                                    tree.getExcepciones().append(result)
                                    tree.updateConsola(result.toString())
                                if isinstance(result,Break): return result
                    if self.instruccionesElse != None:
                        for instr in self.instruccionesElse:
                            result = instr.interpretar(tree,table)
                            if isinstance(result,Excepcion): return result
                            if isinstance(result,Break): return result    
                elif self.instruccionesElse != None:
                    for instr in self.instruccionesElse:
                        result = instr.interpretar(tree,table)
                        if isinstance(result,Excepcion): return result
                        if isinstance(result,Break): return result       
        else:   
           return Excepcion("Semantico","Tipo d e dato no booleano en If.",self.fila,self.columna) 