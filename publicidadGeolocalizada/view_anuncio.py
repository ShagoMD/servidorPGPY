from django.shortcuts import render_to_response
from django.http import HttpResponse;
from utilidades import *;
from django.template import RequestContext;
from api_Anuncio import *;
#import pdb

CAMPOS_REGISTRAR_ANUNCIO=["idPDI","idUser","titulo","descripcion","categoria","URLimagen"]

def peticionRegistrarAnuncio(request):
    if request.method=="POST":
        #pdb.set_trace()
        success, params = extract_params(request.POST,CAMPOS_REGISTRAR_ANUNCIO)
        
        if(success):
            
            registroExitoso=registrarAnuncio(params["idPDI"],params["idUser"],params["titulo"],params["descripcion"],params["categoria"],params["URLimagen"])
            
            if(registroExitoso==1):
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'El PDI al que le quiere agregar el anuncio no le pertenece.'})
            if(registroExitoso==2):            
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Parametros obligatorios vacios.'})
            if(registroExitoso==3):        
                return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Error al guardar el anuncio.'})
            else:                                
                return render_to_json("PDI/respuesta/registroAnuncio.json",{'codigo':100, 'anuncio':registroExitoso}) 
        else:
            return    render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'Los parametros son incorrectos'})
    else:
        return render_to_json("PDI/respuesta/error.json",{'codigo':200, 'mensaje':'No es peticion por POST.'})
                    