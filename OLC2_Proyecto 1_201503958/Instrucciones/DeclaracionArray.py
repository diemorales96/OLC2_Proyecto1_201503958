from Abstract.NodoAST import NodoAST
from typing import Dict
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
class Decla_Array(Instruccion):
    def __init__(self,id,elementos,fila,columna):
        self.id=id
        self.elementos=elementos
        self.fila=fila
        self.columna=columna
        self.tipo=TIPO.ARREGLO
        
    def interpretar(self, tree, table):
        array=[]
        for x in self.elementos:
            if not isinstance(x,Dict):
                if x.tipo!=TIPO.STRUCT:
                    
                    val=x.interpretar(tree,table)
                    val=Simbolo("",x.tipo,False,False,self.fila,self.columna,val)
                    array.append(val)

                else:
                    return Excepcion("Semantico","Tipo de dato incorrecto",self.fila,self.columna)
            else:
                nuevo=self.creararray(x,tree,table)
                array.append(nuevo)
                
        sim=Simbolo(self.id,self.tipo,True,False,self.fila,self.columna,array)
        resul=table.setTabla(sim)
        if isinstance(resul,Excepcion):return resul
        return None

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
        nodo = NodoAST("LLAMADA ARREGLO")
        return nodo