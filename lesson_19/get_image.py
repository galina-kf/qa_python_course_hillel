import requests
from pathlib import Path

image_url = "https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/Getting-Started-with-Testing-in-Python_Watermarked.9f22be97343d.jpg"
response = requests.get(image_url)
url = 'http://127.0.0.1:8080'
image_name = "real_python.jpg"

with open(image_name, "wb") as f:
    f.write(response.content)

file_path = Path(image_name)

with open(file_path, "rb") as f:
    data = {"image": f}
    file_response = requests.post(f'{url}/upload', files=data)

data = file_response.json()
print(file_response.json())
image_url = data.get('image_url')

delete_response = requests.delete(f'{url}/delete/{image_name}')
print(delete_response.status_code)
print(delete_response.json())
