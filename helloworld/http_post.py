
import http.client
import json

conn = http.client.HTTPSConnection('www.httpbin.org')

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

conn.request('POST', '/post', json_data, headers)

response = conn.getresponse()
print(response.read().decode())



import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)
print(r.text)
print(r.json())
r_dictionary= r.json()
print(r_dictionary['form'])