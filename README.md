# flask-supporter

Supported APIs
<pre>
'''
!pip install flask-supporter
#인증 토큰 가져오기
#https://dashboard.ngrok.com/get-started/setup
!ngrok authtoken YOUR_AUTH_TOKEN
'''
import flask_supporter
import pathlib
from .lib_pipeline import TabularRegressionPipeLine

model_path = 'automatethem-com/son-height-tabular-regression-scikit-learn'
p = TabularRegressionPipeLine.from_pretrained(model_path)

try:
    blueprint_file_path = __file__
except:
    blueprint_file_path = None
rest_api = flask_supporter.rest_api.RestAPI(blueprint_file_path, ngrok=False, enable_blueprint_test=True)

def index():
    return '''


def api(x):
    #print(x) #175.0
    #print(type(x)) #<class 'float'>
    x = [
        [x]
    ]

    outputs = p(x)

    #print(outputs) #[{'logit': 170.46931035654347}]
    output = outputs[0]
    #print(output) #{'logit': 170.46931035654347}
    return output

app = rest_api.get_app(index, api)
</pre>
