
TIPO_ENTERO = '1'
TIPO_FLOTANTE = '2'
TIPO_CADENA = '3'


def esTipoValido(variable, tipo):
   tipoValido = True;
   
   try:
        if tipo == TIPO_ENTERO:
            int(variable)
        elif tipo == TIPO_FLOTANTE:
            float(variable)
        elif tipo == TIPO_CADENA:
            str(variable)
   except ValueError:
        tipoValido = False;
        print "Error conversion"
    
   return tipoValido;