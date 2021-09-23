from Abstract.NodoAST import NodoAST
from typing import Dict
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
class Asignar_Array(Instruccion):
    def __init__(self,id,elementos,expresion,fila,columna):
        self.id = id
        self.elementos = elementos
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, tree, table):
        array = table.getTabla(str(self.id))
        array2 = array.getValor()
        value = None
        cont=len(self.elementos)
        numval = 0
        for x in self.elementos:
            if cont>1:
                value=array2[int(x.valor-1)]
                if value.tipo==TIPO.ARREGLO:
                    array2=value.getValor()
            else:
                if not isinstance(self.expresion,Dict):
                    numval=self.expresion.interpretar(tree,table)
                
                    
                if isinstance(numval,Simbolo):
                    a = numval.getValor()
                    numval = Simbolo("",numval.tipo,False,False,self.fila,self.columna,a)
                else:
                    numval = Simbolo("",self.expresion.tipo,False,False,self.fila,self.columna,numval)
                
            cont = cont-1
        arrayprueb = self.actualizar(self.elementos,array.getValor(),tree,table,len(self.elementos),0,numval)
               
        sim=Simbolo(self.id,array.tipo,True,False,self.fila,self.columna,arrayprueb)
        resul=table.actualizarTabla(sim)
        resul=table.getTabla(str(self.id))
        
        if isinstance(resul,Excepcion):return resul
        return None
    def actualizar(self,lista,array,tree,table,max,pos,nuevo):
        if pos<max-1:
            posicion = lista[pos]
            res = posicion.interpretar(tree,table)
            if isinstance(res,Excepcion):return res
            if posicion.tipo==TIPO.ENTERO:
                res = res-1
                if res<0:
                    return Excepcion("Semantico","Posicion fuera del array",self.fila,self.columna)
                array[res]=self.actualizar(lista,array[res].getValor(),tree,table,max,pos+1,nuevo)
                
            return array
        else:
            posicion = lista[pos]
            res = posicion.interpretar(tree,table)
            if isinstance(res,Excepcion):return res
            if posicion.tipo==TIPO.ENTERO:
                n = res-1
                if n<0:
                    return Excepcion("Semantico","Posicion fuera del array",self.fila,self.columna)
                if nuevo.tipo==TIPO.ARREGLO:
                    array[n] = nuevo
                else:
                    if isinstance(array[n],Simbolo):
                        
                        array[n] = nuevo
                        array[n].setTipo(nuevo.tipo)
                    else:
                        array[n] = Simbolo("",self.expresion.tipo,False,False,self.fila,self.columna,nuevo)
                    return array
                    
    def getNodo(self):
        nodo = NodoAST("LLAMADA ARREGLO")
        return nodo