import os
from Instrucciones.Elseif import Elseif
from Instrucciones.Declaracion import Declaracion
from Expresiones.Aritmetica import Aritmetica

from TS.Tipo import OperadorAritmetico, OperadorLogico, OperadorRelacional, TIPO
import sys

sys.setrecursionlimit(3000)

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
    'continue'      : 'RCONTINUE',
    'function'      : 'RFUNCTION',
    'return'        : 'RRETURN',
    'trunc'         : 'RTRUNCATE',
    'log'           : 'RLOG',
    'global'        : 'RGLOBAL',
    'local'         : 'RLOCAL'
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
from Instrucciones.Return import Return
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Expresiones.Truncate import Truncate
from Expresiones.Log import Log 
from Instrucciones.DeclaracionGlobal import DeclaracionGlobal
from Instrucciones.DeclaracionLocal import DeclaracionLocal

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
                        | continue_instr finins
                        | funcion_instr finins
                        | return_instr finins
                        | llamada_instr finins
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
    'imprimir_instr     : RPRINTLN PARA contenidos_print PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))
#Funcion para imprimir en la misma linea
def p_imprimir2(t):
    'imprimir_ins     : RPRINT PARA contenidos_print PARC'
    t[0] = Imprimir2(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_contenidos_print(t):
    'contenidos_print   : contenidos_print COMA valores_print'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_contenidos_print(t):
    'contenidos_print   : valores_print'
    t[0] = [t[1]]

def p_valores_print(t):
    'valores_print  : expresion'
    t[0] = t[1]


def p_declaracion(t):
    ''' declaracion     : declaracion_instr_completa
                        | declaracion_instr_simple
    '''
    t[0] = t[1]

#Declaraciones de variables y asignaciones de valores a variables
def p_declaracion_simple(t):
    ''' declaracion_instr_simple     : ID IGUAL expresion
    '''
    t[0] = Declaracion(t[1],t.lineno(1),find_column(input,t.slice[1]),t[3],None)

def p_declaracion_completa(t):
    '''declaracion_instr_completa   : ID IGUAL expresion DOBLEDPUNTOS tipo
    '''
    t[0] = Declaracion(t[1],t.lineno(1),find_column(input,t.slice[1]),t[3],t[5])


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
    t[0] = If(t[2],t[3],t[6],t[4],t.lineno(1),find_column(input,t.slice[1])) 

def p_if4(t):
    '''if_instr      : RIF expresion instrucciones elseif_instr REND
    '''
    t[0] = If(t[2],t[3],None,t[4],t.lineno(1),find_column(input,t.slice[1]))

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

#Funciones
def p_funcion1(t):
    'funcion_instr    : RFUNCTION ID PARA parametros PARC instrucciones REND'
    t[0] = Funcion(t[2],t[4],t[6],t.lineno(1),find_column(input,t.slice[1]))

def p_funcion_2(t) :
    'funcion_instr     : RFUNCTION ID PARA PARC instrucciones REND'
    t[0] = Funcion(t[2],[], t[5], t.lineno(1), find_column(input, t.slice[1]))
#Parametros
def p_parametros_1(t):
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_2(t):
    'parametros      : parametro'
    t[0] = [t[1]]
#Parametro
def p_parametro(t):
    'parametro      : ID DOBLEDPUNTOS tipo'
    t[0] = {'tipo':t[3],'identificador':t[1]}
#Return
def p_return(t) :
    'return_instr     : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))
#Llamadas
def p_llamada1(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1],[], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada2(t) :
    'llamada_instr     : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
#Parametros
def p_parametrosLL_1(t) :
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]
#Parametro
def p_parametrosLL_2(t) :
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]

def p_parametroLL(t) :
    'parametro_llamada     : expresion'
    t[0] = t[1]

#Global
def p_declaracion2(t):
    'declaracion    : RGLOBAL ID IGUAL expresion'
    t[0] = DeclaracionGlobal(t[2],t.lineno(1),find_column(input,t.slice[1]),None,t[4])

def p_declaracion2_global(t):
    'declaracion    : RGLOBAL ID'
    t[0] = DeclaracionGlobal(t[2],t.lineno(1),find_column(input,t.slice[1]),None,t[4])
#Local
def p_declaracion_local(t):
    'declaracion    : RLOCAL ID IGUAL expresion'
    t[0] = DeclaracionLocal(t[2],t.lineno(1), find_column(input,t.slice[1]),None,t[4])

def p_declaracion_local2(t):
    'declaracion    : RLOCAL ID'
    t[0] = DeclaracionLocal(t[2],t.lineno(1),find_column(input,t.slice[1]),None,None)


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

def p_expresion_llamada(t):
    '''expresion : llamada_instr'''
    t[0] = t[1]

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

def p_expresion_truncate(t):
    'expresion  : RTRUNCATE PARA RINT COMA expresion PARC'
    t[0] = Truncate(t[5],t.lineno(1),find_column(input,t.slice[1]))

def p_expresion_log(t):
    'expresion : RLOG PARA expresion COMA expresion PARC'
    t[0] = Log(t[3],t[5],t.lineno(1),find_column(input,t.slice[1]))

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

def ReporteTabla(Errores):
    cadena = "{% extends \"layout.html\" %}\n{% block content %}\n\n"
    cadena = cadena + "<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">"
    cadena = cadena + "<div class=\"collapse navbar-collapse\" id=\"navbarNav\">\n"
    cadena = cadena + "<ul class=\"navbar-nav\">\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena  = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/Reportes\">Reporte de Errores</a>\n"
    cadena  = cadena + "</li>\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "</li>"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/TablaSimbolos\">Tabla de Simbolos</a>\n"
    cadena  = cadena + "</li>\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "</li>"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/Arbol\">Arbol de Analisis Sintactico</a>\n"
    cadena = cadena + "</li>"
    cadena = cadena + "</ul>"
    cadena = cadena + "</div>"
    cadena  = cadena + "</nav>"
    cadena = cadena + "<center>\n<table style=\"text-align:center;\" border=\"2\" class = \"egt\">\n\t"
    cadena = cadena + "\n\t\t<th>No.</th>\n\t\t<th>Descripcion</th>\n\t\t<th>Linea</th>\n\t\t<th>Columna</th>\n\t\t<th>Fecha y Hora</th>\n\t</tr>\n" 
    cont = 1
    for a in Errores:
        cadena = cadena + "<tr>\n\t\t<td>"+ str(cont) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a.descripcion +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a.fila) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a.columna) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a.fecha +"</td>\n"
        cont += 1
    
    cadena = cadena +"</table>\n{% endblock %}"
    crearArchivo(cadena,"./templates/")

def crearArchivo(cadena,path):
        try:
            os.stat(path.strip())
        except:
            os.makedirs(path.strip())
        with open(path+"Reportes.html","w+",encoding="utf-8") as file:
            file.seek(0,0)
            file.write(cadena)
            file.close()
        #END
#END


def ReporteTSimbolos(Tabla):
    cadena = "{% extends \"layout.html\" %}\n{% block content %}\n\n"
    cadena = cadena + "<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">"
    cadena = cadena + "<div class=\"collapse navbar-collapse\" id=\"navbarNav\">\n"
    cadena = cadena + "<ul class=\"navbar-nav\">\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena  = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/Reportes\">Reporte de Errores</a>\n"
    cadena  = cadena + "</li>\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "</li>"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/TablaSimbolos\">Tabla de Simbolos</a>\n"
    cadena  = cadena + "</li>\n"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "</li>"
    cadena = cadena + "<li class=\"nav-item\">\n"
    cadena = cadena + "<a class=\"nav-link active\" aria-current=\"page\" href=\"/Arbol\">Arbol de Analisis Sintactico</a>\n"
    cadena = cadena + "</li>"
    cadena = cadena + "</ul>"
    cadena = cadena + "</div>"
    cadena  = cadena + "</nav>"
    cadena = cadena + "<center>\n<table border=\"1\" class = \"egt\">\n\t"
    cadena = cadena + "<tr>\n\t\t<th>Nombre</th>\n\t\t<th>Tipo</th>\n\t\t<th>Ambito</th>\n\t\t<th>Fila</th>\n\t\t<th>Columna</th>\n\t</tr>\n" 
    cont = 1
    for a in Tabla:
        cadena = cadena + "<tr>\n\t\t<td>"+ a[0] +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a[1] +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ a[2] +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a[3]) +"</td>\n"
        cadena = cadena + "\n\t\t<td>"+ str(a[4]) +"</td>\n"
        cont += 1
    
    cadena = cadena +"</table>\n{% endblock %}"
    crearArchivo2(cadena,"./templates/")


def crearArchivo2(cadena,path):
        try:
            os.stat(path.strip())
        except:
            os.makedirs(path.strip())
        with open(path+"TablaSimbolos.html","w+",encoding="utf-8") as file:
            file.seek(0,0)
            file.write(cadena)
            file.close()
        #END
#END


from Nativas.Lowercase import Lowercase
from Nativas.Uppercase import Uppercase
from Nativas.Typeof import Typeof
from Nativas.Log10 import Log10
from Nativas.Sin import Sin
from Nativas.Cos import Cos
from Nativas.Tan import Tan
from Nativas.Sqrt import Sqrt
from Nativas.Float import Float

def crearNativas(ast):         
    nombre = "uppercase"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'uppercase##Param1'}]
    instrucciones = []
    uppercase = Uppercase(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(uppercase)     

    nombre = "lowercase"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'lowercase##Param1'}]
    instrucciones = []
    lower = Lowercase(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(lower)

    nombre = "typeof"
    parametros = [{'tipo':TIPO.NULO,'identificador':'typeof##param1'}] 
    instrucciones = []
    typeof = Typeof(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(typeof)

    nombre = "log10"
    parametros = [{'tipo':TIPO.NULO,'identificador':'log10##param1'}] 
    instrucciones = []
    log10 = Log10(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(log10)

    nombre = "sin"
    parametros = [{'tipo':TIPO.NULO,'identificador':'sin##param1'}] 
    instrucciones = []
    sin = Sin(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(sin)

    nombre = "cos"
    parametros = [{'tipo':TIPO.NULO,'identificador':'cos##param1'}] 
    instrucciones = []
    cos = Cos(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(cos)

    nombre = "tan"
    parametros = [{'tipo':TIPO.NULO,'identificador':'tan##param1'}] 
    instrucciones = []
    tan = Tan(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(tan)

    nombre = "sqrt"
    parametros = [{'tipo':TIPO.NULO,'identificador':'sqrt##param1'}] 
    instrucciones = []
    sqrt = Sqrt(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(sqrt)

    nombre = "float"
    parametros = [{'tipo':TIPO.NULO,'identificador':'float##param1'}] 
    instrucciones = []
    float = Float(nombre,parametros,instrucciones,-1,-1)
    ast.addFuncion(float)

f = open("./src/entrada.txt", "r")
entrada = f.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodoAST import NodoAST
instrucciones = parse(entrada)
ast = Arbol(instrucciones)

TSGlobal = TablaSimbolos(None,"GLOBAL")
ast.setTSglobal(TSGlobal)
TSGlobal.limpiarTabla()
crearNativas(ast)

for error in errores:
    ast.getExcepciones().append(error)
    ast.updateConsola(error.toString())
    
#Primera pasada para poder guardar las funciones existentes
for instruccion in ast.getInstrucciones():
    if isinstance(instruccion, Funcion):
        TSGlobal.setTSimbolos(instruccion)
        ast.addFuncion(instruccion)

    if isinstance(instruccion,Declaracion):
        ast.addGlobal(instruccion)
#Segunda pasada para realizar todas las acciones excepto las declaraciones de funcones que ya se hicieron en la primera pasada
for instruccion in ast.getInstrucciones():
    if not isinstance(instruccion,Funcion):
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Excepcion) :
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString()) 

init = NodoAST("RAIZ")
instr = NodoAST("INSTRUCCIONES")

for instruccion in ast.getInstrucciones():
    instr.agregarHijoNodo(instruccion.getNodo())

init.agregarHijoNodo(instr)
graph = ast.getDot(init)
dirname = os.path.dirname(__file__)
direcc = os.path.join(dirname, 'ast.dot')
file = open(direcc, "w+", encoding="utf-8")
file.write(graph)
file.close()
os.chdir(dirname)
os.system('dot -T svg -o ast.svg ast.dot')

print(ast.getConsola())
#def Analizar(entrada):

    #ReporteTabla(ast.getExcepciones())
    #tabla = TSGlobal.obtenerTSimbolos()
    #ReporteTSimbolos(tabla)
    #return ast.getConsola()
    
