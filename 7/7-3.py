import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }


    response = requests.get("https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_{}{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    print(content)

    # containers = content.find('span', {})
get_exchange_rate('USD', 'KRW')
