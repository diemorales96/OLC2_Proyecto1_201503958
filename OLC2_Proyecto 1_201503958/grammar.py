from Instrucciones.Elseif import Elseif
from Instrucciones.Declaracion import Declaracion
from Expresiones.Aritmetica import Aritmetica

from TS.Tipo import OperadorAritmetico, OperadorLogico, OperadorRelacional, TIPO
import re
import sys

from TS.Excepcion import Excepcion
#-------------------------------------------------ANALISIS LEXICO--------------------------------------------
errores = []
reservadas = {
    'println'       : 'RPRINTLN',
    'print'         : 'RPRINT',
    'false'         : 'RFALSE',
    'true'          : 'RTRUE',
    'Int64'         : 'RINT',
    'Float64'       : 'RDOUBLE',
    'nothing'       : 'RNULO',
    'Bool'          : 'RBOOLEAN',
    'Char'          : 'RCHAR',
    'String'        : 'RSTRING',
    'if'            : 'RIF',
    'else'          : 'RELSE',
    'end'           : 'REND',
    'else'          : 'RELSE',
    'elseif'        : 'RELSEIF',
    'while'         : 'RWHILE',
    'for'           : 'RFOR',
    'in'            : 'RIN',
    'parse'         : 'RPARSE',
    'break'         : 'RBREAK',
    'continue'      : 'RCONTINUE'
}

tokens = [
    'PARA',
    'PARC',
    'PUNTOCOMA',
    'CADENA',
    'CARACTER',
    'ID',
    'DECIMAL',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIV',
    'POR',
    'POT',
    'MOD',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'NOT',
    'AND',
    'OR',
    'IGUAL',
    'DOBLEDPUNTOS',
    'DOSPUNTOS',
    'COMA'
]+list(reservadas.values())

t_PARA          = r'\('
t_PARC          = r'\)'
t_PUNTOCOMA     = r';'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'/'
t_POT           = r'\^'
t_MOD           = r'%'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_IGUALIGUAL    = r'=='
t_DIFERENTE     = r'!='
t_NOT           = r'!'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_IGUAL         = r'='
t_DOBLEDPUNTOS  = r'::'
t_DOSPUNTOS     = r':'
t_COMA          = r','

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_COMENTARIO_MULT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID')
     return t

def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_CARACTER(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|[^\\\'\"])?\'"""
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.lex as lex
lexer = lex.lex()

#-------------------------------------------------ANALISIS SINTACTICO--------------------------------------------


from Expresiones.Primitivos import Primitivos
from Expresiones.Identificador import Identificador
from Instrucciones.Imprimir import Imprimir
from Instrucciones.imprimir2 import Imprimir2
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.For import For
from Expresiones.Casteo import Casteo
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','MENORQUE','MAYORQUE', 'IGUALIGUAL','DIFERENTE','MENORIGUAL','MAYORIGUAL'), 
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MOD'),
    ('nonassoc','POT'),
    ('right','UMENOS'),
    )

#Inicio y lista de las instrucciones que pueden venir
def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion      : imprimir_instr finins
                        | imprimir_ins finins
                        | declaracion finins
                        | if_instr finins
                        | while_instr finins
                        | for_instr finins
                        | break_instr finins
                        | continue_instr
    '''
    t[0] = t[1]
#Fin de la instruccion (termina con ;)
def p_finins(t):
    '''finins       : PUNTOCOMA'''
    t[0] = None
#Error y se recupera con ;
def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintactico","Error Sintactico." + str(t[1].value),t.lineno(1),find_column(input,t.slice[1])))
    t[0] = ""
#Funcion para imprimir con salto de linea
def p_imprimir(t):
    'imprimir_instr     : RPRINTLN PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))
#Funcion para imprimir en la misma linea
def p_imprimir2(t):
    'imprimir_ins     : RPRINT PARA expresion PARC'
    t[0] = Imprimir2(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion(t):
    ''' declaracion     : declaracion_instr_completa
                        | declaracion_instr_simple
    '''
    t[0] = t[1]
#if
def p_if1(t):
    '''if_instr     : RIF expresion instrucciones REND
    '''
    t[0] = If(t[2],t[3],None,None,t.lineno(1),find_column(input,t.slice[1]))

#if else
def p_if2(t):
    '''if_instr     : RIF expresion instrucciones RELSE instrucciones REND
    '''
    t[0] = If(t[2],t[3],t[5],None,t.lineno(1),find_column(input,t.slice[1]))   

# if elseif else
def p_if3(t):
    '''if_instr      : RIF expresion instrucciones elseif_instr RELSE instrucciones REND
    '''
    t[0] = t[0] = If(t[2],t[3],t[6],t[4],t.lineno(1),find_column(input,t.slice[1])) 
#lista de elseif
def p_elsif(t):
    '''elseif_instr     : elseif_instr elseif_instruction
    '''
    if t[2] !="":
        t[1].append(t[2])
    t[0] = t[1]

def p_elseif_instr(t):
    '''elseif_instr     : elseif_instruction
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_elseif_instruction(t):
    '''elseif_instruction   : RELSEIF expresion instrucciones 
    '''
    t[0] = Elseif(t[2],t[3],t.lineno(1),find_column(input,t.slice[1]))

#While

def p_while(t):
    '''while_instr : RWHILE expresion instrucciones REND
    '''
    t[0] = While(t[2],t[3],t.lineno(1),find_column(input,t.slice[1]))
#for
def p_for(t):
    '''for_instr    : RFOR ID RIN expresion DOSPUNTOS expresion instrucciones REND
    '''
    t[0] = For(t[2],t[4],t[6],t[7],None,t.lineno(1),find_column(input,t.slice[1]))

def p_for2(t):
    '''for_instr    : RFOR ID RIN expresion instrucciones REND
    '''
    t[0] = For(t[2],None,None,t[5],t[4],t.lineno(1),find_column(input,t.slice[1]))
#break
def p_break(t):
    '''break_instr  : RBREAK
    '''
    t[0] = Break(t.lineno(1),find_column(input,t.slice[1]))

#continue
def p_continue(t):
    '''continue_instr   : RCONTINUE
    '''
    t[0] = Continue(t.lineno(1),find_column(input,t.slice[1]))

#Declaraciones de variables y asignaciones de valores a variables
def p_declaracion_simple(t):
    ''' declaracion_instr_simple     : ID IGUAL expresion
    '''
    t[0] = Declaracion(t[1],t.lineno(1),find_column(input,t.slice[1]),t[3],None)

def p_declaracion_completa(t):
    '''declaracion_instr_completa   : ID IGUAL expresion DOBLEDPUNTOS tipo
    '''
    t[0] = Declaracion(t[1],t.lineno(1),find_column(input,t.slice[1]),t[3],t[5])

#Tipos de variables
def p_tipo(t) :
    '''tipo     : RINT
                | RDOUBLE
                | RCHAR
                | RSTRING
                | RBOOLEAN '''
    if t[1] == 'Int64':
        t[0] = TIPO.ENTERO
    elif t[1] == 'Float64':
        t[0] = TIPO.DECIMAL
    elif t[1] == 'String':
       t[0] = TIPO.CADENA
    elif t[1] == 'BooL':
        t[0] = TIPO.BOOLEANO
    elif t[1] == 'Char':
        t[0] = TIPO.CARACTER


#Operaciones Binarias entre 2 expresiones
def p_expresion_binaria(t):
    '''
    expresion   : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion POT expresion
                | expresion MOD expresion
                | expresion MENORQUE expresion
                | expresion MAYORQUE expresion
                | expresion MENORIGUAL expresion
                | expresion MAYORIGUAL expresion
                | expresion IGUALIGUAL expresion
                | expresion DIFERENTE expresion
                | expresion OR expresion
                | expresion AND expresion
                | expresion COMA expresion
    '''
    if t[2] == "+":
        t[0] =  Aritmetica(OperadorAritmetico.MAS, t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "-":
        t[0] = Aritmetica(OperadorAritmetico.MENOS,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "*":
        t[0] = Aritmetica(OperadorAritmetico.POR,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "/":
        t[0] = Aritmetica(OperadorAritmetico.DIV,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "^":
        t[0] = Aritmetica(OperadorAritmetico.POT,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "%":
        t[0] = Aritmetica(OperadorAritmetico.MOD,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "<":
        t[0] = Relacional(OperadorRelacional.MENORQUE,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == ">":
        t[0] = Relacional(OperadorRelacional.MAYORQUE,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "<=":
        t[0] = Relacional(OperadorRelacional.MENORIGUAL,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == ">=":
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "==":
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "!=":    
        t[0] = Relacional(OperadorRelacional.DIFERENTE,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "||":
        t[0] = Logica(OperadorLogico.OR,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == "&&":
        t[0] = Logica(OperadorLogico.AND,t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == ",":
        t[0] =  Aritmetica(OperadorAritmetico.CONCATENACION, t[1],t[3],t.lineno(2),find_column(input,t.slice[2]))
#Expresiones Unarias
def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS
              | NOT expresion %prec UNOT 
    '''
    if t[1] == "-":
        t[0] = Aritmetica(OperadorAritmetico.UMENOS,t[2],None,t.lineno(1),find_column(input,t.slice[1]))
    elif t[1] == "!":
        t[0] = Logica(OperadorLogico.NOT,t[2],None,t.lineno(1),find_column(input,t.slice[1]))
#Agrupacion por parentesis de una expresion 
def p_expresion_agrupacion(t):
    '''
    expresion   : PARA expresion PARC
    '''
    t[0] = t[2]

#Otos tipos de expresiones
def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_caracter(t):
    '''expresion : CARACTER'''
    t[0] = Primitivos(TIPO.CARACTER,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cast(t):
    '''expresion : RPARSE PARA tipo COMA expresion PARC
    '''
    t[0] = Casteo(t[3],t[5],t.lineno(1),find_column(input,t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()
input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

f = open("./entrada.txt", "r")
entrada = f.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

instrucciones = parse(entrada)
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)

for error in errores:
    ast.getExcepciones().append(error)
    
for instruccion in ast.getInstrucciones():
    value = instruccion.interpretar(ast,TSGlobal)
    if isinstance(value, Excepcion) :
        ast.getExcepciones().append(value)
        ast.updateConsola(value.toString())

print(ast.getConsola())