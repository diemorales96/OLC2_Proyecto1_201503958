import re
import sys

errores = []
reservadas = {
    'print'     : 'RPRINT',
    'var'       : 'RVAR',
    'int64'     : 'RINT',
    'float64'   : 'RFLOAT',
    'nothing'   : 'NULO',
    'bool'      : 'RBOOL',
    'char'      : 'RCHAR',
    'string'    : 'RSTRING',
          

}

tokens = [
    'PARA',
    'PARC',
    'CORA',
    'CORC',
    'LLAVEA',
    'LLAVEC',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'PUNTOCOMA',
    'CADENA',
    'CARACTER',
    'ID',
    'DECIMAL',
    'ENTERO',
    'IGUAL',
]+list(reservadas.values())

t_PARA          = r'\('
t_PARC          = r'\)'
t_CORA          = r'\['
t_CORC          = r'\]'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIV           = r'/'
t_POT           = r'^'
t_MOD           = r'%'
t_PUNTOCOMA     = r';'

