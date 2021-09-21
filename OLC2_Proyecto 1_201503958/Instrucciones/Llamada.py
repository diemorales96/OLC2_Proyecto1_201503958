from TS.Tipo import TIPO
from TS.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Abstract.NodoAST import NodoAST

class Llamada(Instruccion):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        self.funcion = False
        self.param = True 

    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre) 
        if result == None: 
            return Excepcion("Semantico", "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)
        
        nuevaTabla = TablaSimbolos(tree.getTSGlobal(),self.nombre,None)
        if len(result.parametros) == len(self.parametros): 
           contador=0
           for expresion in self.parametros: 
                resultExpresion = expresion.interpretar(tree, table)
                if isinstance(resultExpresion, Excepcion): return resultExpresion
                if (result.parametros[contador]['identificador'] == "truncate##param1")or (result.parametros[contador]['identificador'] == "typeof##param1") or (result.parametros[contador]['identificador']=="log10##param1")or (result.parametros[contador]['identificador']=="sin##param1")or (result.parametros[contador]['identificador']=="cos##param1")or (result.parametros[contador]['identificador']=="tan##param1")or (result.parametros[contador]['identificador']=="sqrt##param1")or (result.parametros[contador]['identificador']=="float##param1"):
                    result.parametros[contador]["tipo"] = expresion.tipo
                if result.parametros[contador]["tipo"] == expresion.tipo or result.parametros[contador]["tipo"] == TIPO.ARREGLO: 
                    if result.parametros[contador]['tipo'] == TIPO.ARREGLO:
                        self.arreglo = True
                        simbolo = Simbolo(str(result.parametros[contador]['identificador']),expresion.tipo,self.arreglo,self.funcion,self.fila,self.columna,resultExpresion)
                    else:
                        simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipo'],self.arreglo,self.funcion, self.fila, self.columna, resultExpresion,self.param)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion): return resultTabla
                 
                else:
                    return Excepcion("Semantico", "Tipo de dato diferente en Parametros de la llamada.", self.fila, self.columna)
                contador += 1 
        else: 
            return Excepcion("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
        value = result.interpretar(tree, nuevaTabla)   
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo
        return value

    def getNodo(self):
        nodo = NodoAST("LLAMADA A FUNCION")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoAST("PARAMETROS")
        for param in self.parametros:
            parametros.agregarHijoNodo(param.getNodo())
        nodo.agregarHijoNodo(parametros)
        return nodo