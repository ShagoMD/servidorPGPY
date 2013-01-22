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