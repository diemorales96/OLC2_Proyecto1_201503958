from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from TS.Tipo import TIPO
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:  
                    nuevaTabla = TablaSimbolos(table)      
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Continue): return None
                        #if isinstance(result, Return): return result
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
            