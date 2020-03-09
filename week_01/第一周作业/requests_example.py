import requests

get_response = requests.get('http://httpbin.org/get')
json_data = get_response.json()
print('json result of get: {0}'.format(json_data))

post_response = requests.post('http://httpbin.org/post')
json_data = post_response.json()
print('json result of post: {0}'.format(json_data))
