# submitting a web form.

import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Michael', 'lname': 'Herman'}

#submit post request

r = requests.post(url, data=data)

print r.content