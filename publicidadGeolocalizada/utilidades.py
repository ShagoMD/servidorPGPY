from django.shortcuts import render_to_response

def _extract_params(request, fields, mandatory=False):
    
    fields_dict = {}

    for field in fields:
        if not field in request:
            if mandatory:
                return False, field
        else:
            fields_dict[field] = request[field]

    return True, fields_dict

def extract_params(request, mandatory_fields, optional_fields=None):
    params = {}
    params_opt = {}
    
    success, params = _extract_params (request, mandatory_fields, True)
    
    if not success:
        return False, params

    if optional_fields != None:
        success, params_opt = _extract_params (request, optional_fields, False)
        params.update(params_opt)
    
    return True, params

def render_to_json(*args, **kwargs):
    
    response = render_to_response(*args, **kwargs)
    #response['mimetype'] = "application/json"
    response['Pragma'] = "no cache"
    response['Cache-Control'] = "no-cache, must-revalidate"
    response['Content-Type'] = "application/json"

    return response