from concurrent.futures import ThreadPoolExecutor
import requests

count=0

def spam():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://pbpwm.sqnbzf.biz.id',
        'Connection': 'keep-alive',
        'Referer': 'https://pbpwm.sqnbzf.biz.id/index.php?gToken=verified',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
        'playid': '1030612204',
        'PhoneNumber': '082125007456',
        'level': '59',
        'tier': 'Epic',
        'email': '082125007456',
        'password': 'sayang',
        'login': 'Facebook',
    }

    response = requests.post('https://pbpwm.sqnbzf.biz.id/data.php', headers=headers, data=data)

    print(response.status_code)


for i in range(1000000):
    with ThreadPoolExecutor(max_workers=30) as th:
        for i in range(100):
            th.submit(spam)