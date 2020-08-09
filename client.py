import requests

url = "http://127.0.0.1:5000/"

print(f"Sending a get request to the following url: {url}")

response_get = requests.get(url).text
print(f"Received as response: {response_get}")

input_1 = {"base": "5", "exponent": "2"}

print(f"Sending a post request to the same url with the following JSON: {input_1}")
response_post = requests.post(url, json=input_1).text
print(f"Received as response: {response_post}")

input_2 = {"base": "2", "exponent": "3"}

print(f"Sending a post request to the same url with the following JSON: {input_2}")
response_post = requests.post(url, json=input_2).text
print(f"Received as response: {response_post}")
