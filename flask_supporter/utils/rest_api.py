from flask import Flask
from flask import request
import flask_ngrok
from flask import Blueprint
import pathlib
from flask import request
import json
import base64
import io
from PIL import Image
import re

def image_to_base64(image):
    bytesIO = io.BytesIO()
    try:
        image.save(bytesIO, "JPEG")
    except:
        image.save(bytesIO, "PNG")
    b64encoded = base64.b64encode(bytesIO.getvalue())
    base64_str = b64encoded.decode("utf-8")
    return base64_str

class RestAPI():
    def __init__(self, ngrok=True, enable_blueprint_test=True):
        super().__init__()
        self.MODE_NGROK_FLASK = 1
        self.MODE_BLUEPRINT = 2
        self.MODE = self.MODE_BLUEPRINT
        self.ENABLE_BLUEPRINT_TEST = True

        if self.MODE == self.MODE_NGROK_FLASK:
            self.app = Flask(__name__)
            self.index_url = '/'
            self.api_url = '/api'
        elif self.MODE == self.MODE_BLUEPRINT:
            self.folder_name = pathlib.Path(__file__).parts[-2]
            #print(self.folder_name) #son_height_tabular_regression_scikit_learn
            self.folder_name = self.folder_name.replace('_', '-')
            #print(self.folder_name) #son-height-tabular-regression-scikit-learn
            self.index_url = f'/{self.folder_name}/'
            self.api_url = f'/{self.folder_name}/api'
            
    def get_urls(self):
        return self.index_url, self.api_url
        
    def get_app(self, index_function, api_function):
        if self.MODE == self.MODE_NGROK_FLASK:
            app = Flask(__name__)
        elif self.MODE == self.MODE_BLUEPRINT:
            app = Blueprint(self.folder_name, __name__)
    
        if self.MODE == self.MODE_NGROK_FLASK or (self.MODE == self.MODE_BLUEPRINT and self.ENABLE_BLUEPRINT_TEST):
            @app.route(self.index_url)
            def index():
                return index_function()
            
        @app.route(self.api_url, methods=['post'])
        def api():
            return self.predict(request, api_function)
    
        if __name__ == "__main__":
            if self.MODE == self.MODE_NGROK_FLASK:
                flask_ngrok.run_with_ngrok(app)
                app.run()
    
        return app

    def is_float(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def preprocess(self, d):
        #print(d['file']) #iVBORw...w9RndTMZLiy1AAAAABJRU5ErkJggg==
        #print(type(d['file'])) #<class 'str'>
        d_ = {}
        for key in d:
            value = d[key]
            if value.startswith('data:') : #Image
                #print(value) #data:image/jpeg;base64,/9j/4TT...
                value = value.replace("data:", "") #data url 부분 제거
                value = re.sub('^.+,', '', value) 
                #print(value) #/9j/4TT...
                bytes = base64.b64decode(value) 
                bytesIO = io.BytesIO(bytes)
                value = Image.open(bytesIO)
            elif self.is_float(value):
                value = float(value)
            d_[key] = value
        return d_

    def postprocess(self, d):
        d_ = {}
        for key in d:
            value = d[key]
            if str(type(value)) == "<class 'PIL.PngImagePlugin.PngImageFile'>": 
                value = image_to_base64(value)
            d_[key] = value
        return d_

    def predict(self, request, predict_function):
        payload = request.get_json()
        data = payload['data']
        #print(data) #[{'a': 1, 'b': 2}]
        postprocessed_examples = []
        for example in data:
            preprocessed_example = self.preprocess(example)
            #print(example) #{'file': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=561x561 at 0x7F8457E79A30>}
            output_example = predict_function(**preprocessed_example)
            postprocessed_example = self.postprocess(output_example)
            postprocessed_examples.append(postprocessed_example)
        j = json.dumps({'data': postprocessed_examples})
        return j
