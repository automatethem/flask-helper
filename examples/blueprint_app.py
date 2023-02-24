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
rest_api = flask_supporter.rest_api.RestAPI(blueprint_file_path, ngrok=True, enable_blueprint_test=True)

def index():
    return '''
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form id="form">
            x <input type="text" name="x" value="175"><br>
            <!--<input type="file" id="file"><br>-->
            <input type="submit">
        </form>
        <div id="result">예측 결과</div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script>
/*
var base64String;
$("#file").on("change", (event) => {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onloadend = () => {
        base64String = reader.result
        //console.log(base64String); //data:image/jpeg;base64,/9j/4TT...
    };
    reader.readAsDataURL(file);
});
*/
$('#form').submit((event) => {
    event.preventDefault(); //폼 제출 방지
    var data = {'data': [
            {
                'x': $("input[name=x]").val(),
                //'file': base64String
            }
        ]
    };
    $.ajax("{{api_url}}", {
        type: "POST",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: (data) => {
            if (typeof(data) == "object")
                data = JSON.stringify(data);
            //var d = JSON.parse(data);
            //$("#result").text(d);
            $("#result").text(data);
            console.log(data);
        }
    });
});
        </script>
    </body>
</html>
    '''.replace('{{api_url}}', rest_api.api_url)

#REST API 송신 데이터 예: {"data": [{"x": "175"}]}
#REST API 수신 데이터 예: {"data": [{"logit": 175.99442286524624}]}
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
