from flask import request
from flask import jsonify
import base64
import io
from PIL import Image

def preprocess(d):
    #print(d['file']) #iVBORw...w9RndTMZLiy1AAAAABJRU5ErkJggg==
    #print(type(d['file'])) #<class 'str'>
    d_ = {}
    for key in d:
        value = d[key]
        #'''
        if value.endswith('==') : #Image
            bytes = base64.b64decode(value) 
            bytesIO = io.BytesIO(bytes)
            value = Image.open(bytesIO)
        #'''
        d_[key] = value
    return d_

def postprocess(d):
    d_ = {}
    for key in d:
        value = d[key]
        d_[key] = value
    return d_

def rest_api(request, predict_function):
    d = request.get_json()
    #d = {'a': 1, 'b': 2}
    
    d = preprocess(d)
    #print(d) #{'file': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=561x561 at 0x7F8457E79A30>}
    d = predict_function(**d)
    d = postprocess(d)

    json = jsonify(d)
    return json
