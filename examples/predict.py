import rest_api_supporter

#url = 'https://automatethem.pythonanywhere.com:8000/apis/son-height-tabular-regression-api'
url = 'http://localhost:8000/apis/son-height-tabular-regression-api'

payload = {'data': [{'x': 175}]}
#print(payload) #{'data': [{'x': 175}]}
outputs = rest_api_supporter.utils.query(url, json=payload)
#outputs = {'data': [{'logit': 175.99442286524624}]} #query(url, json=payload)
#print(outputs) #{'data': [{'logit': 175.99442286524624}]}
result = outputs['data'][0]['logit']
print(result) #175.99442286524624
