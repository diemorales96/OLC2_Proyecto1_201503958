from datetime import datetime
class Excepcion:
    def __init__(self, tipo, descripcion, fila, columna):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna
        now = datetime.now()
        self.fecha = str(now.day)+"/"+str(now.month)+"/"+str(now.year)+","+str(now.hour) +":"+ str(now.minute) +":"+ str(now.second)

    def toString(self):
        return self.tipo + " - " + self.descripcion + " [" + str(self.fila) + "," + str(self.columna) + "]" + "--" + self.fecha

    