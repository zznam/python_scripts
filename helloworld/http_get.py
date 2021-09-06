import http.client
import pprint
import requests

connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
print(connection)

connection = http.client.HTTPSConnection("www.journaldev.com")
connection.request("GET", "/")
response = connection.getresponse()

print("Status: {} and reason: {}".format(response.status, response.reason))

headers = response.getheaders()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))

connection.close()

r = requests.get('https://xkcd.com/1906/')
print(r.status_code)
print(r.headers)
print(r.text)

receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
with open(r'D:\workspace\image5.png','wb') as f:
    f.write(receive.content)


ploads = {'things':2,'total':25}
r = requests.get('https://httpbin.org/get',params=ploads)
print(r.text)
print(r.url)