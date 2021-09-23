from Expresiones.Identificador import Identificador
from typing import Dict
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from Abstract.NodoAST import NodoAST
class Length(Instruccion):
    def __init__(self,id,elementos,fila,columna):
        self.id = id
        self.elementos = elementos
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.ARREGLO
        
    def interpretar(self, tree, table):
        array=table.getTabla(str(self.id))
        array2 = array.getValor()
        val=None
        contador=len(self.elementos)
        nval=0
        
        for x in self.elementos:
            if contador>1:
                if isinstance(x,Identificador):
                    x=x.interpretar(tree,table)
                    val=array2[int(x-1)]
                else:
                    val=array2[int(x.valor-1)]
                if val.tipo==TIPO.ARREGLO:
                    array2=val.getValor()
            else:
                if isinstance(x,Identificador):
                    x=x.interpretar(tree,table)
                    val=array2[int(x-1)]
                else:
                    val=array2[int(x.valor-1)]
               
                array2=val.getValor()
                
            contador=contador-1
        nval=len(array2)
        sim=Simbolo("",TIPO.ENTERO,False,False,self.fila,self.columna,nval)
        return sim

    def creararray(self,datos,tree,table):
        array=[]
        if isinstance(datos,Dict):
            if datos['tipo']==TIPO.ARREGLO:
                nuev=self.creararray(datos['valores'],tree,table)
                ar2=nuev
        else:
            ar=[]
            for r in datos:
                if not isinstance(r,Dict):
                    f=r.interpretar(tree,table)
                    sim=Simbolo("",r.tipo,False,False,self.fila,self.columna,f)
                    ar.append(sim)
                else:
                    nuevito=self.creararray(r,tree,table)
                    ar.append(nuevito)
            ar2=Simbolo("",TIPO.ARREGLO,True,False,self.fila,self.columna,ar)
            
        return ar2
    
    def getNodo(self):
        nodo = NodoAST("LENGTH")
        return nodo