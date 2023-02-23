import requests
import re

url = 'https://m.blog.naver.com/act41/221578376673'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers)
# print(response.text)

result = re.findall(r'[\w.-]+@[\w.-]+', response.text)
result = list(set(result))

print(result)