import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'dXUJ4zNFWwM13mplfBAAvqGdAdnFU29Xo1iOAs28'}
#params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


response = requests.get(url=url)

status_code = response.status_code
text = response.text
headers = dict(response.headers)

print(status_code)
print(headers)
print(text)
print(response.json())