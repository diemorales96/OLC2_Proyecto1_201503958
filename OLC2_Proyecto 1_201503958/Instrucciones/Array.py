from Abstract.NodoAST import NodoAST
from typing import Dict
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
class Array(Instruccion):
    def __init__(self,id,elementos,fila,columna):
        self.id=id
        self.elementos=elementos
        self.fila=fila
        self.columna=columna
        self.tipo=TIPO.ARREGLO
        
    def interpretar(self, tree, table):
        array=table.getTabla(str(self.id))
        array2=array.getValor()
        val=None
        contador=len(self.elementos)
        nval=0
        for x in self.elementos:
            if contador>1:
                val=array2[int(x.valor-1)]
                if val.tipo==TIPO.ARREGLO:
                    array2=val.getValor()
            else:
                nval=x.interpretar(tree,table)
                
            contador=contador-1
        arrayprueb=self.actualizar(self.elementos,array.getValor(),tree,table,len(self.elementos),0,nval)
        if arrayprueb.tipo!=TIPO.ARREGLO:
            self.tipo = arrayprueb.tipo
            return arrayprueb
        return arrayprueb

    def actualizar(self,lista,array,tree,table,max,pos,nuevo):
        if pos<max-1:
            posicion=lista[pos]
            res=posicion.interpretar(tree,table)
            if isinstance(res,Excepcion):return res
            if posicion.tipo==TIPO.ENTERO:
                res=res-1
                if res<0:
                    return Excepcion("Semantico","Posicion fuera del array",self.fila,self.columna)
                valor=self.actualizar(lista,array[res].getValor(),tree,table,max,pos+1,nuevo)
                
            return valor
        else:
            posicion=lista[pos]
            res=posicion.interpretar(tree,table)
            if isinstance(res,Excepcion):return res
            if posicion.tipo==TIPO.ENTERO:
                n=res-1
                if n<0:
                    return Excepcion("Semantico","Posicion fuera del array",self.fila,self.columna)
                val=array[n]
                return val
    def getNodo(self):
        nodo = NodoAST("LLAMADA ARREGLO")
        return nodo