import rest_api_supporter

url = 'https://automatethem.pythonanywhere.com/son-height-tabular-regression-scikit-learn/api'

user_input = 175
payload = {'data': [{'x': str(user_input)}]}
outputs = rest_api_supporter.utils.query(url, json=payload)
#print(outputs) #{'data': [{'logit': 175.99442286524624}]}
result = outputs['data'][0]['logit']
print(result)
