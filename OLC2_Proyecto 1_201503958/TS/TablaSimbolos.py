from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} 
        self.anterior = anterior

        
    def setTabla(self, simbolo): 
        if simbolo.id in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id] = simbolo
            return None    
                    

    def getTabla(self, id):        
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]   
            else:
                tablaActual = tablaActual.anterior
        return None

    def getTablasLocales(self, id):        
        tablaActual = self
        while tablaActual.anterior != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]   
            else:
                tablaActual = tablaActual.anterior
        return None    

    def actualizarGlobal(self,simbolo):
        tablaActual = self
        while tablaActual.anterior != None:
            tablaActual = tablaActual.anterior
        tablaActual.tabla[simbolo.identificador].setValor(simbolo.expresion.valor)
        return None


    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id].getTipo() == simbolo.getTipo():
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None
                elif tablaActual.tabla[simbolo.id].getTipo() == TIPO.NULO:
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None
                elif simbolo.getValor() == None:
                    tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())

            else:
                tablaActual = tablaActual.anterior
            
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
