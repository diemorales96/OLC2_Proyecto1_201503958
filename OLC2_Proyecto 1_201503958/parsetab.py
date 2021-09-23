
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftMENORQUEMAYORQUEIGUALIGUALDIFERENTEMENORIGUALMAYORIGUALleftMASMENOSleftDIVPORMODnonassocPOTrightUMENOSAND CADENA CARACTER COMA CORA CORC DECIMAL DIFERENTE DIV DOBLEDPUNTOS DOSPUNTOS ENTERO ID IGUAL IGUALIGUAL MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MOD NOT OR PARA PARC POR POT PUNTOCOMA RARRAY RBOOLEAN RBREAK RCHAR RCONTINUE RDOUBLE RELSE RELSEIF REND RFALSE RFOR RFUNCTION RGLOBAL RIF RIN RINT RLENGTH RLOCAL RLOG RNULO RPARSE RPRINT RPRINTLN RRETURN RSTRING RTRUE RTRUNCATE RWHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr finins\n                        | imprimir_ins finins\n                        | declaracion finins\n                        | if_instr finins\n                        | while_instr finins\n                        | for_instr finins\n                        | break_instr finins\n                        | continue_instr finins\n                        | funcion_instr finins\n                        | return_instr finins\n                        | llamada_instr finins\n    finins       : PUNTOCOMAinstruccion        : error PUNTOCOMAimprimir_instr     : RPRINTLN PARA contenidos_print PARCimprimir_ins     : RPRINT PARA contenidos_print PARCcontenidos_print   : contenidos_print COMA valores_printcontenidos_print   : valores_printvalores_print  : expresion declaracion     : declaracion_instr_completa\n                        | declaracion_instr_simple\n                        | decla_arr\n                        | acces\n     declaracion_instr_simple     : ID IGUAL expresion\n    declaracion_instr_completa   : ID IGUAL expresion DOBLEDPUNTOS tipo\n    if_instr     : RIF expresion instrucciones REND\n    if_instr     : RIF expresion instrucciones RELSE instrucciones REND\n    if_instr      : RIF expresion instrucciones elseif_instr RELSE instrucciones REND\n    if_instr      : RIF expresion instrucciones elseif_instr REND\n    elseif_instr     : elseif_instr elseif_instruction\n    elseif_instr     : elseif_instruction\n    elseif_instruction   : RELSEIF expresion instrucciones \n    while_instr : RWHILE expresion instrucciones REND\n    for_instr    : RFOR ID RIN expresion DOSPUNTOS expresion instrucciones REND\n    for_instr    : RFOR ID RIN expresion instrucciones REND\n    break_instr  : RBREAK\n    continue_instr   : RCONTINUE\n    funcion_instr    : RFUNCTION ID PARA parametros PARC instrucciones RENDfuncion_instr     : RFUNCTION ID PARA PARC instrucciones RENDparametros     : parametros COMA parametroparametros      : parametroparametro      : ID DOBLEDPUNTOS tiporeturn_instr     : RRETURN expresionllamada_instr     : ID PARA PARCllamada_instr     : ID PARA parametros_llamada PARCparametros_llamada     : parametros_llamada COMA parametro_llamadaparametros_llamada    : parametro_llamadaparametro_llamada     : expresiondeclaracion    : RGLOBAL ID IGUAL expresiondeclaracion    : RGLOBAL IDdeclaracion    : RLOCAL ID IGUAL expresiondeclaracion    : RLOCAL IDdecla_arr : ID IGUAL elementelement : element CORA elementos CORCelement : CORA elementos CORCelementos : elementos COMA elementos2elementos : elementos2elementos2 : expresionexpresion : CORA elementos CORCacces : ID corchetes IGUAL expresioncorchetes : corchetes CORA expre CORCcorchetes : CORA expre CORCexpre : expresionexpresion : ID recursrecurs : recurs CORA unico CORCrecurs : CORA unico CORCunico : expresiontipo     : RINT\n                | RDOUBLE\n                | RCHAR\n                | RSTRING\n                | RBOOLEAN \n                | RARRAY\n    expresion   : expresion MAS expresion\n                | expresion MENOS expresion\n                | expresion POR expresion\n                | expresion DIV expresion\n                | expresion POT expresion\n                | expresion MOD expresion\n                | expresion MENORQUE expresion\n                | expresion MAYORQUE expresion\n                | expresion MENORIGUAL expresion\n                | expresion MAYORIGUAL expresion\n                | expresion IGUALIGUAL expresion\n                | expresion DIFERENTE expresion\n                | expresion OR expresion\n                | expresion AND expresion\n    \n    expresion : MENOS expresion %prec UMENOS\n              | NOT expresion %prec UNOT \n    \n    expresion   : PARA expresion PARC\n    expresion : llamada_instrexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : CARACTERexpresion : RTRUEexpresion : RFALSEexpresion : RPARSE PARA tipo COMA expresion PARC\n    expresion  : RTRUNCATE PARA RINT COMA expresion PARCexpresion : RLOG PARA expresion COMA expresion PARCexpresion : RLENGTH PARA ID PARC'
    
_lr_action_items = {'error':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[15,15,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,15,-94,-93,-95,-96,-97,-98,-99,-100,15,-46,15,-66,-90,-91,15,-47,15,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,15,15,15,15,15,-68,-104,15,15,15,15,15,-67,15,15,-101,-102,-103,15,]),'RPRINTLN':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[16,16,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,16,-94,-93,-95,-96,-97,-98,-99,-100,16,-46,16,-66,-90,-91,16,-47,16,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,16,16,16,16,16,-68,-104,16,16,16,16,16,-67,16,16,-101,-102,-103,16,]),'RPRINT':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[17,17,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,17,-94,-93,-95,-96,-97,-98,-99,-100,17,-46,17,-66,-90,-91,17,-47,17,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,17,17,17,17,17,-68,-104,17,17,17,17,17,-67,17,17,-101,-102,-103,17,]),'RGLOBAL':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[22,22,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,22,-94,-93,-95,-96,-97,-98,-99,-100,22,-46,22,-66,-90,-91,22,-47,22,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,22,22,22,22,22,-68,-104,22,22,22,22,22,-67,22,22,-101,-102,-103,22,]),'RLOCAL':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[24,24,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,24,-94,-93,-95,-96,-97,-98,-99,-100,24,-46,24,-66,-90,-91,24,-47,24,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,24,24,24,24,24,-68,-104,24,24,24,24,24,-67,24,24,-101,-102,-103,24,]),'RIF':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[25,25,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,25,-94,-93,-95,-96,-97,-98,-99,-100,25,-46,25,-66,-90,-91,25,-47,25,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,25,25,25,25,25,-68,-104,25,25,25,25,25,-67,25,25,-101,-102,-103,25,]),'RWHILE':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[26,26,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,26,-94,-93,-95,-96,-97,-98,-99,-100,26,-46,26,-66,-90,-91,26,-47,26,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,26,26,26,26,26,-68,-104,26,26,26,26,26,-67,26,26,-101,-102,-103,26,]),'RFOR':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[27,27,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,27,-94,-93,-95,-96,-97,-98,-99,-100,27,-46,27,-66,-90,-91,27,-47,27,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,27,27,27,27,27,-68,-104,27,27,27,27,27,-67,27,27,-101,-102,-103,27,]),'RBREAK':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[28,28,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,28,-94,-93,-95,-96,-97,-98,-99,-100,28,-46,28,-66,-90,-91,28,-47,28,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,28,28,28,28,28,-68,-104,28,28,28,28,28,-67,28,28,-101,-102,-103,28,]),'RCONTINUE':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[29,29,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,29,-94,-93,-95,-96,-97,-98,-99,-100,29,-46,29,-66,-90,-91,29,-47,29,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,29,29,29,29,29,-68,-104,29,29,29,29,29,-67,29,29,-101,-102,-103,29,]),'RFUNCTION':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[30,30,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,30,-94,-93,-95,-96,-97,-98,-99,-100,30,-46,30,-66,-90,-91,30,-47,30,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,30,30,30,30,30,-68,-104,30,30,30,30,30,-67,30,30,-101,-102,-103,30,]),'RRETURN':([0,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,54,56,60,61,62,63,64,65,66,71,80,92,110,112,113,119,126,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,174,182,183,186,189,193,195,197,199,202,203,204,208,211,215,216,217,218,],[31,31,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,31,-94,-93,-95,-96,-97,-98,-99,-100,31,-46,31,-66,-90,-91,31,-47,31,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,31,31,31,31,31,-68,-104,31,31,31,31,31,-67,31,31,-101,-102,-103,31,]),'ID':([0,2,3,22,24,25,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,52,54,55,56,57,58,59,60,61,62,63,64,65,66,71,79,80,86,87,88,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,110,111,112,113,117,118,119,120,121,123,126,127,129,136,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,159,171,174,182,183,186,189,190,191,192,193,194,195,197,198,199,202,203,204,208,211,215,216,217,218,],[23,23,-3,48,53,56,56,72,73,56,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,56,56,56,56,56,23,56,-94,56,56,56,-93,-95,-96,-97,-98,-99,-100,23,56,-46,56,56,56,56,23,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-66,56,-90,-91,56,169,23,56,172,56,-47,56,56,23,56,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,56,56,-92,23,23,23,23,23,-68,56,56,56,-104,56,23,23,172,23,23,23,-67,23,23,-101,-102,-103,23,]),'$end':([1,2,3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,],[0,-1,-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,]),'REND':([3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,92,119,137,138,182,185,195,199,202,203,211,218,],[-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,135,170,184,-33,201,-32,209,213,214,-34,219,220,]),'RELSE':([3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,92,137,138,185,203,],[-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,136,183,-33,-32,-34,]),'RELSEIF':([3,32,33,34,35,36,37,38,39,40,41,42,43,44,45,92,137,138,185,203,],[-3,-2,-4,-15,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-16,139,139,-33,-32,-34,]),'PUNTOCOMA':([4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,21,28,29,48,53,56,60,61,62,63,64,65,66,74,80,84,85,110,112,113,122,124,125,126,131,134,135,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,161,162,163,164,165,166,170,178,180,184,189,193,200,201,204,209,213,214,215,216,217,219,220,],[34,34,34,34,34,34,34,34,34,34,34,45,-22,-23,-24,-25,-38,-39,-52,-54,-94,-93,-95,-96,-97,-98,-99,-100,-45,-46,-26,-55,-66,-90,-91,-17,-18,-51,-47,-62,-53,-28,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,-70,-71,-72,-73,-74,-75,-35,-27,-57,-31,-68,-104,-56,-29,-67,-37,-41,-30,-101,-102,-103,-40,-36,]),'PARA':([16,17,23,25,26,31,46,47,49,50,52,55,56,57,58,59,67,68,69,70,73,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[46,47,49,59,59,59,59,59,59,59,59,59,49,59,59,59,115,116,117,118,121,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'IGUAL':([23,48,51,53,133,181,],[50,79,87,91,-64,-63,]),'CORA':([23,25,26,31,46,47,49,50,51,52,55,56,57,58,59,79,85,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,110,111,117,120,123,127,129,133,139,155,156,180,181,189,190,191,192,194,200,204,],[52,55,55,55,55,55,55,86,88,55,55,111,55,55,55,55,129,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,156,55,55,55,55,55,55,-64,55,55,55,-57,-63,-68,55,55,55,55,-56,-67,]),'MENOS':([25,26,31,46,47,49,50,52,54,55,56,57,58,59,60,61,62,63,64,65,66,71,74,77,79,80,83,84,86,87,88,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,109,110,111,112,113,114,117,120,123,125,126,127,129,131,134,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,158,159,168,171,180,186,189,190,191,192,193,194,204,205,206,207,208,215,216,217,],[57,57,57,57,57,57,57,57,94,57,-94,57,57,57,-93,-95,-96,-97,-98,-99,-100,94,94,94,57,-46,94,94,57,57,57,94,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,94,-66,57,-90,94,94,57,57,57,94,-47,57,57,94,94,57,-76,-77,-78,-79,-80,-81,94,94,94,94,94,94,94,94,-61,57,57,94,-92,94,94,-61,94,-68,57,57,57,-104,57,-67,94,94,94,94,-101,-102,-103,]),'NOT':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'ENTERO':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'DECIMAL':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'CADENA':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'CARACTER':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'RTRUE':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'RFALSE':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'RPARSE':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'RTRUNCATE':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'RLOG':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'RLENGTH':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'PARC':([49,56,60,61,62,63,64,65,66,75,76,77,78,80,81,82,83,110,112,113,114,121,126,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,161,162,163,164,165,166,169,173,175,176,177,189,193,204,205,206,207,210,212,215,216,217,],[80,-94,-93,-95,-96,-97,-98,-99,-100,122,-20,-21,124,-46,126,-49,-50,-66,-90,-91,159,174,-47,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,-70,-71,-72,-73,-74,-75,193,197,-43,-19,-48,-68,-104,-67,215,216,217,-44,-42,-101,-102,-103,]),'MAS':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[93,-94,-93,-95,-96,-97,-98,-99,-100,93,93,93,-46,93,93,93,93,-66,-90,93,93,93,-47,93,93,-76,-77,-78,-79,-80,-81,93,93,93,93,93,93,93,93,-61,93,-92,93,93,-61,93,-68,-104,-67,93,93,93,93,-101,-102,-103,]),'POR':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[95,-94,-93,-95,-96,-97,-98,-99,-100,95,95,95,-46,95,95,95,95,-66,-90,95,95,95,-47,95,95,95,95,-78,-79,-80,-81,95,95,95,95,95,95,95,95,-61,95,-92,95,95,-61,95,-68,-104,-67,95,95,95,95,-101,-102,-103,]),'DIV':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[96,-94,-93,-95,-96,-97,-98,-99,-100,96,96,96,-46,96,96,96,96,-66,-90,96,96,96,-47,96,96,96,96,-78,-79,-80,-81,96,96,96,96,96,96,96,96,-61,96,-92,96,96,-61,96,-68,-104,-67,96,96,96,96,-101,-102,-103,]),'POT':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[97,-94,-93,-95,-96,-97,-98,-99,-100,97,97,97,-46,97,97,97,97,-66,-90,97,97,97,-47,97,97,97,97,97,97,None,97,97,97,97,97,97,97,97,97,-61,97,-92,97,97,-61,97,-68,-104,-67,97,97,97,97,-101,-102,-103,]),'MOD':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[98,-94,-93,-95,-96,-97,-98,-99,-100,98,98,98,-46,98,98,98,98,-66,-90,98,98,98,-47,98,98,98,98,-78,-79,-80,-81,98,98,98,98,98,98,98,98,-61,98,-92,98,98,-61,98,-68,-104,-67,98,98,98,98,-101,-102,-103,]),'MENORQUE':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[99,-94,-93,-95,-96,-97,-98,-99,-100,99,99,99,-46,99,99,99,99,-66,-90,99,99,99,-47,99,99,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,99,99,-61,99,-92,99,99,-61,99,-68,-104,-67,99,99,99,99,-101,-102,-103,]),'MAYORQUE':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[100,-94,-93,-95,-96,-97,-98,-99,-100,100,100,100,-46,100,100,100,100,-66,-90,100,100,100,-47,100,100,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,100,100,-61,100,-92,100,100,-61,100,-68,-104,-67,100,100,100,100,-101,-102,-103,]),'MENORIGUAL':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[101,-94,-93,-95,-96,-97,-98,-99,-100,101,101,101,-46,101,101,101,101,-66,-90,101,101,101,-47,101,101,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,101,101,-61,101,-92,101,101,-61,101,-68,-104,-67,101,101,101,101,-101,-102,-103,]),'MAYORIGUAL':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[102,-94,-93,-95,-96,-97,-98,-99,-100,102,102,102,-46,102,102,102,102,-66,-90,102,102,102,-47,102,102,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,102,102,-61,102,-92,102,102,-61,102,-68,-104,-67,102,102,102,102,-101,-102,-103,]),'IGUALIGUAL':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[103,-94,-93,-95,-96,-97,-98,-99,-100,103,103,103,-46,103,103,103,103,-66,-90,103,103,103,-47,103,103,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,103,103,-61,103,-92,103,103,-61,103,-68,-104,-67,103,103,103,103,-101,-102,-103,]),'DIFERENTE':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[104,-94,-93,-95,-96,-97,-98,-99,-100,104,104,104,-46,104,104,104,104,-66,-90,104,104,104,-47,104,104,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,104,104,-61,104,-92,104,104,-61,104,-68,-104,-67,104,104,104,104,-101,-102,-103,]),'OR':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[105,-94,-93,-95,-96,-97,-98,-99,-100,105,105,105,-46,105,105,105,105,-66,-90,-91,105,105,-47,105,105,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,105,-92,105,105,-61,105,-68,-104,-67,105,105,105,105,-101,-102,-103,]),'AND':([54,56,60,61,62,63,64,65,66,71,74,77,80,83,84,90,109,110,112,113,114,125,126,131,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,158,159,168,171,180,186,189,193,204,205,206,207,208,215,216,217,],[106,-94,-93,-95,-96,-97,-98,-99,-100,106,106,106,-46,106,106,106,106,-66,-90,-91,106,106,-47,106,106,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,106,-89,-61,106,-92,106,106,-61,106,-68,-104,-67,106,106,106,106,-101,-102,-103,]),'COMA':([56,60,61,62,63,64,65,66,75,76,77,78,80,81,82,83,107,108,109,110,112,113,126,130,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,160,161,162,163,164,165,166,167,168,173,175,176,177,179,187,189,193,204,210,212,215,216,217,],[-94,-93,-95,-96,-97,-98,-99,-100,123,-20,-21,123,-46,127,-49,-50,155,-59,-60,-66,-90,-91,-47,155,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,190,-70,-71,-72,-73,-74,-75,191,192,198,-43,-19,-48,155,-58,-68,-104,-67,-44,-42,-101,-102,-103,]),'DOBLEDPUNTOS':([56,60,61,62,63,64,65,66,80,84,110,112,113,126,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,172,180,189,193,204,215,216,217,],[-94,-93,-95,-96,-97,-98,-99,-100,-46,128,-66,-90,-91,-47,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,196,-61,-68,-104,-67,-101,-102,-103,]),'CORC':([56,60,61,62,63,64,65,66,80,89,90,107,108,109,110,112,113,126,130,132,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,157,158,159,179,187,188,189,193,204,215,216,217,],[-94,-93,-95,-96,-97,-98,-99,-100,-46,133,-65,154,-59,-60,-66,-90,-91,-47,180,181,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,189,-69,-92,200,-58,204,-68,-104,-67,-101,-102,-103,]),'DOSPUNTOS':([56,60,61,62,63,64,65,66,80,110,112,113,126,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,159,171,189,193,204,215,216,217,],[-94,-93,-95,-96,-97,-98,-99,-100,-46,-66,-90,-91,-47,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-61,-92,194,-68,-104,-67,-101,-102,-103,]),'RIN':([72,],[120,]),'RINT':([115,116,128,196,],[161,167,161,161,]),'RDOUBLE':([115,128,196,],[162,162,162,]),'RCHAR':([115,128,196,],[163,163,163,]),'RSTRING':([115,128,196,],[164,164,164,]),'RBOOLEAN':([115,128,196,],[165,165,165,]),'RARRAY':([115,128,196,],[166,166,166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,54,71,136,171,174,183,186,197,208,],[2,92,119,182,195,199,202,203,211,218,]),'instruccion':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[3,32,3,3,32,32,3,3,3,32,3,3,32,3,32,32,32,3,32,32,]),'imprimir_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'imprimir_ins':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'declaracion':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'if_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'while_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'for_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'break_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'continue_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'funcion_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'return_instr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'llamada_instr':([0,2,25,26,31,46,47,49,50,52,54,55,57,58,59,71,79,86,87,88,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,119,120,123,127,129,136,139,155,156,171,174,182,183,186,190,191,192,194,195,197,199,202,203,208,211,218,],[14,14,60,60,60,60,60,60,60,60,14,60,60,60,60,14,60,60,60,60,60,14,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,14,60,60,60,60,14,60,60,60,14,14,14,14,14,60,60,60,60,14,14,14,14,14,14,14,14,]),'declaracion_instr_completa':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'declaracion_instr_simple':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'decla_arr':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'acces':([0,2,54,71,92,119,136,171,174,182,183,186,195,197,199,202,203,208,211,218,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'finins':([4,5,6,7,8,9,10,11,12,13,14,],[33,35,36,37,38,39,40,41,42,43,44,]),'corchetes':([23,],[51,]),'expresion':([25,26,31,46,47,49,50,52,55,57,58,59,79,86,87,88,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,111,117,120,123,127,129,139,155,156,190,191,192,194,],[54,71,74,77,77,83,84,90,109,112,113,114,125,109,131,90,134,140,141,142,143,144,145,146,147,148,149,150,151,152,153,158,168,171,77,83,109,186,109,158,205,206,207,208,]),'contenidos_print':([46,47,],[75,78,]),'valores_print':([46,47,123,],[76,76,176,]),'parametros_llamada':([49,],[81,]),'parametro_llamada':([49,127,],[82,177,]),'element':([50,],[85,]),'expre':([52,88,],[89,132,]),'elementos':([55,86,129,],[107,130,179,]),'elementos2':([55,86,129,155,],[108,108,108,187,]),'recurs':([56,],[110,]),'elseif_instr':([92,],[137,]),'elseif_instruction':([92,137,],[138,185,]),'unico':([111,156,],[157,188,]),'tipo':([115,128,196,],[160,178,210,]),'parametros':([121,],[173,]),'parametro':([121,198,],[175,212,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',213),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',217),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',223),
  ('instruccion -> imprimir_instr finins','instruccion',2,'p_instruccion','grammar.py',230),
  ('instruccion -> imprimir_ins finins','instruccion',2,'p_instruccion','grammar.py',231),
  ('instruccion -> declaracion finins','instruccion',2,'p_instruccion','grammar.py',232),
  ('instruccion -> if_instr finins','instruccion',2,'p_instruccion','grammar.py',233),
  ('instruccion -> while_instr finins','instruccion',2,'p_instruccion','grammar.py',234),
  ('instruccion -> for_instr finins','instruccion',2,'p_instruccion','grammar.py',235),
  ('instruccion -> break_instr finins','instruccion',2,'p_instruccion','grammar.py',236),
  ('instruccion -> continue_instr finins','instruccion',2,'p_instruccion','grammar.py',237),
  ('instruccion -> funcion_instr finins','instruccion',2,'p_instruccion','grammar.py',238),
  ('instruccion -> return_instr finins','instruccion',2,'p_instruccion','grammar.py',239),
  ('instruccion -> llamada_instr finins','instruccion',2,'p_instruccion','grammar.py',240),
  ('finins -> PUNTOCOMA','finins',1,'p_finins','grammar.py',245),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',249),
  ('imprimir_instr -> RPRINTLN PARA contenidos_print PARC','imprimir_instr',4,'p_imprimir','grammar.py',254),
  ('imprimir_ins -> RPRINT PARA contenidos_print PARC','imprimir_ins',4,'p_imprimir2','grammar.py',258),
  ('contenidos_print -> contenidos_print COMA valores_print','contenidos_print',3,'p_contenidos_print','grammar.py',262),
  ('contenidos_print -> valores_print','contenidos_print',1,'p_lista_contenidos_print','grammar.py',267),
  ('valores_print -> expresion','valores_print',1,'p_valores_print','grammar.py',271),
  ('declaracion -> declaracion_instr_completa','declaracion',1,'p_declaracion','grammar.py',276),
  ('declaracion -> declaracion_instr_simple','declaracion',1,'p_declaracion','grammar.py',277),
  ('declaracion -> decla_arr','declaracion',1,'p_declaracion','grammar.py',278),
  ('declaracion -> acces','declaracion',1,'p_declaracion','grammar.py',279),
  ('declaracion_instr_simple -> ID IGUAL expresion','declaracion_instr_simple',3,'p_declaracion_simple','grammar.py',285),
  ('declaracion_instr_completa -> ID IGUAL expresion DOBLEDPUNTOS tipo','declaracion_instr_completa',5,'p_declaracion_completa','grammar.py',290),
  ('if_instr -> RIF expresion instrucciones REND','if_instr',4,'p_if1','grammar.py',297),
  ('if_instr -> RIF expresion instrucciones RELSE instrucciones REND','if_instr',6,'p_if2','grammar.py',303),
  ('if_instr -> RIF expresion instrucciones elseif_instr RELSE instrucciones REND','if_instr',7,'p_if3','grammar.py',309),
  ('if_instr -> RIF expresion instrucciones elseif_instr REND','if_instr',5,'p_if4','grammar.py',314),
  ('elseif_instr -> elseif_instr elseif_instruction','elseif_instr',2,'p_elsif','grammar.py',320),
  ('elseif_instr -> elseif_instruction','elseif_instr',1,'p_elseif_instr','grammar.py',327),
  ('elseif_instruction -> RELSEIF expresion instrucciones','elseif_instruction',3,'p_elseif_instruction','grammar.py',335),
  ('while_instr -> RWHILE expresion instrucciones REND','while_instr',4,'p_while','grammar.py',342),
  ('for_instr -> RFOR ID RIN expresion DOSPUNTOS expresion instrucciones REND','for_instr',8,'p_for','grammar.py',347),
  ('for_instr -> RFOR ID RIN expresion instrucciones REND','for_instr',6,'p_for2','grammar.py',352),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',359),
  ('continue_instr -> RCONTINUE','continue_instr',1,'p_continue','grammar.py',365),
  ('funcion_instr -> RFUNCTION ID PARA parametros PARC instrucciones REND','funcion_instr',7,'p_funcion1','grammar.py',371),
  ('funcion_instr -> RFUNCTION ID PARA PARC instrucciones REND','funcion_instr',6,'p_funcion_2','grammar.py',375),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros_1','grammar.py',379),
  ('parametros -> parametro','parametros',1,'p_parametros_2','grammar.py',384),
  ('parametro -> ID DOBLEDPUNTOS tipo','parametro',3,'p_parametro','grammar.py',388),
  ('return_instr -> RRETURN expresion','return_instr',2,'p_return','grammar.py',392),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada1','grammar.py',396),
  ('llamada_instr -> ID PARA parametros_llamada PARC','llamada_instr',4,'p_llamada2','grammar.py',400),
  ('parametros_llamada -> parametros_llamada COMA parametro_llamada','parametros_llamada',3,'p_parametrosLL_1','grammar.py',404),
  ('parametros_llamada -> parametro_llamada','parametros_llamada',1,'p_parametrosLL_2','grammar.py',409),
  ('parametro_llamada -> expresion','parametro_llamada',1,'p_parametroLL','grammar.py',413),
  ('declaracion -> RGLOBAL ID IGUAL expresion','declaracion',4,'p_declaracion2','grammar.py',418),
  ('declaracion -> RGLOBAL ID','declaracion',2,'p_declaracion2_global','grammar.py',422),
  ('declaracion -> RLOCAL ID IGUAL expresion','declaracion',4,'p_declaracion_local','grammar.py',426),
  ('declaracion -> RLOCAL ID','declaracion',2,'p_declaracion_local2','grammar.py',430),
  ('decla_arr -> ID IGUAL element','decla_arr',3,'p_decla_array','grammar.py',435),
  ('element -> element CORA elementos CORC','element',4,'p_elemen','grammar.py',439),
  ('element -> CORA elementos CORC','element',3,'p_elemen2','grammar.py',444),
  ('elementos -> elementos COMA elementos2','elementos',3,'p_elementos','grammar.py',448),
  ('elementos -> elementos2','elementos',1,'p_elementos2','grammar.py',453),
  ('elementos2 -> expresion','elementos2',1,'p_elementos3','grammar.py',457),
  ('expresion -> CORA elementos CORC','expresion',3,'p_expresionarray','grammar.py',461),
  ('acces -> ID corchetes IGUAL expresion','acces',4,'p_accesarr','grammar.py',465),
  ('corchetes -> corchetes CORA expre CORC','corchetes',4,'p_corchetes','grammar.py',469),
  ('corchetes -> CORA expre CORC','corchetes',3,'p_corchetes2','grammar.py',474),
  ('expre -> expresion','expre',1,'p_corchetes3','grammar.py',478),
  ('expresion -> ID recurs','expresion',2,'p_acceso_array','grammar.py',482),
  ('recurs -> recurs CORA unico CORC','recurs',4,'p_acceso_array2','grammar.py',485),
  ('recurs -> CORA unico CORC','recurs',3,'p_acceso_array3','grammar.py',489),
  ('unico -> expresion','unico',1,'p_acceso_array4','grammar.py',493),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',498),
  ('tipo -> RDOUBLE','tipo',1,'p_tipo','grammar.py',499),
  ('tipo -> RCHAR','tipo',1,'p_tipo','grammar.py',500),
  ('tipo -> RSTRING','tipo',1,'p_tipo','grammar.py',501),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','grammar.py',502),
  ('tipo -> RARRAY','tipo',1,'p_tipo','grammar.py',503),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',521),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',522),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',523),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','grammar.py',524),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',525),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','grammar.py',526),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',527),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',528),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',529),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',530),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',531),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','grammar.py',532),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',533),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',534),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',568),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',569),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',578),
  ('expresion -> llamada_instr','expresion',1,'p_expresion_llamada','grammar.py',583),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',588),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',592),
  ('expresion -> DECIMAL','expresion',1,'p_primitivo_decimal','grammar.py',596),
  ('expresion -> CADENA','expresion',1,'p_primitivo_cadena','grammar.py',600),
  ('expresion -> CARACTER','expresion',1,'p_primitivo_caracter','grammar.py',604),
  ('expresion -> RTRUE','expresion',1,'p_primitivo_true','grammar.py',608),
  ('expresion -> RFALSE','expresion',1,'p_primitivo_false','grammar.py',612),
  ('expresion -> RPARSE PARA tipo COMA expresion PARC','expresion',6,'p_expresion_cast','grammar.py',616),
  ('expresion -> RTRUNCATE PARA RINT COMA expresion PARC','expresion',6,'p_expresion_truncate','grammar.py',621),
  ('expresion -> RLOG PARA expresion COMA expresion PARC','expresion',6,'p_expresion_log','grammar.py',625),
  ('expresion -> RLENGTH PARA ID PARC','expresion',4,'p_expresion_length','grammar.py',633),
]
