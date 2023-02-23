from flask import request
from flask import jsonify

def preprocess(d):
    d_ = {}
    for key in d:
        value = d[key]
        d_[key] = value
    return d

def postprocess(d):
    d_ = {}
    for key in d:
        value = d[key]
        #if value == : #Image
        #    pass
        d_[key] = value
    return d

def rest_api(request, predict_function):
    d = request.get_json()
    #d = {'a': 1, 'b': 2}
    
    d = preprocess(d)
    d = predict_function(**d)
    d = postprocess(d)

    json = jsonify(d)
    return json
