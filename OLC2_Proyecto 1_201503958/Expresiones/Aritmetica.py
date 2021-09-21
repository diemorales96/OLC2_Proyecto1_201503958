from io import open_code
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO,OperadorAritmetico
from Abstract.NodoAST import NodoAST

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperaicionDer,fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperaicionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None


    def interpretar(self, tree, table):

        #Verifica si vienen ambos operadores
        izq = self.OperacionIzq.interpretar(tree,table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree,table)
            if isinstance(der,Excepcion):return der
        #END
        #Verifica tipo de operacion a realizar
        #----------------------------------------------------------------------SUMA-----------------------------------------------------------------------------------
        if self.operador == OperadorAritmetico.MAS:
            #Verifica tipos de los operadores(ENTEROS/DECIMALES/STRING/etc...)
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                #Coloca un tipo al resultado
                self.tipo = TIPO.ENTERO
                #Retorna resultado 
                return self.obtenerVal(self.OperacionIzq.tipo,izq) + self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) + self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) + self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) + self.obtenerVal(self.OperacionDer.tipo,der)
            else:
                return Excepcion("Semantico", "Null pointer para expresion +.", self.fila,self.columna)
            #END
        #----------------------------------------------------------------------RESTA-----------------------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.MENOS:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo,izq) - self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) - self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) - self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) - self.obtenerVal(self.OperacionDer.tipo,der)
            else:
                return Excepcion("Semantico", "Null pointer para expresion -.", self.fila,self.columna)
            #END
        #------------------------------------------------------------------MULTIPLICACION-------------------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.POR:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo,izq) * self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) * self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) * self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) * self.obtenerVal(self.OperacionDer.tipo,der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo,izq) + self.obtenerVal(self.OperacionDer.tipo,der)
            else:
                return Excepcion("Semantico", "Null pointer para expresion *.", self.fila,self.columna)
            #END
        #------------------------------------------------------------------DIVISION------------------------------------------------------------------------------
        elif self.operador == OperadorAritmetico.DIV:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) / self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) / self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) / self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) / self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            else:
                return Excepcion("Semantico", "Null pointer para expresion /.", self.fila,self.columna)
            #END
        #------------------------------------------------------------------POTENCIA------------------------------------------------------------------------------        
        elif self.operador == OperadorAritmetico.POT:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo,izq) ** self.obtenerVal(self.OperacionDer.tipo,der)               
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) ** self.obtenerVal(self.OperacionDer.tipo,der)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) ** self.obtenerVal(self.OperacionDer.tipo,der)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo,izq) ** self.obtenerVal(self.OperacionDer.tipo,der)
                #END
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.CADENA
                cad = ""
                for i in range(self.obtenerVal(self.OperacionDer.tipo,der)):
                    cad = cad + self.obtenerVal(self.OperacionIzq.tipo,izq)
                return cad
            else:
                return Excepcion("Semantico", "Null pointer para expresion /.", self.fila,self.columna)
            #END
        #------------------------------------------------------------------MODULAR------------------------------------------------------------------------------        
        elif self.operador == OperadorAritmetico.MOD:
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.ENTERO
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) % self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) % self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) % self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                if self.obtenerVal(self.OperacionDer.tipo,der) != 0:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo,izq) % self.obtenerVal(self.OperacionDer.tipo,der)
                else:
                    return Excepcion("Semantico", "El divisor no puede ser 0", self.fila,self.columna)
                #END
            else:
                return Excepcion("Semantico", "Null pointer para expresion /.", self.fila,self.columna)
            #END
        #------------------------------------------------------------------UMENOS------------------------------------------------------------------------------        
        elif self.operador == OperadorAritmetico.UMENOS:
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
        else:
            return Excepcion("Semantico", "Operador no definido.", self.fila,self.columna)
        #END
    #END

    def getNodo(self):
        nodo = NodoAST("ARITMETICA")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        else:
            nodo.agregarHijo(self.operador)
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
        return nodo


    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
            