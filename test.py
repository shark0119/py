import json
import sys
from os.path import getsize
import requests


def test_sys_args():
    argv = sys.argv
    args = len(argv)
    if args >= 2:
        if argv[1] == "--help":
            print("[file_path] [expected size(GB)]")

    if args >= 3:
        file = argv[1]
        amount = int(int(argv[2]) * 1024 * 1024 / getsize(file))
    elif args == 2:
        file = argv[1]

    print(amount)
    print(getsize(file))


def test_login():
    login_params = {"country": 86,
                    "cellphone": "15556925243",
                    "password": "asdf1234",
                    "captcha": "",
                    "remember": 1,
                    "platform": 3,
                    'appid': 1}
    url = "https://account.geekbang.org/account/ticket/login"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8;zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': '111',
        'Content-type': 'application/json',
        'Cookie': 'ga=GA1.2.210210018.1532048329; GCID=4efcf01-ef7777c-1372b32-349e601; hibext_instdsigdipv2=1; _gid=GA1.2.1753971063.1539913605',
        'Host': "account.geekbang.org",
        'Referer': 'https://account.geekbang.org/singin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    }
    session = requests.Session()
    resp = session.post(url, data=json.dumps(login_params), headers=headers)
    if resp.status_code == 200:
        resp.encoding = resp.apparent_encoding
        print('login success:' + resp.content.decode("utf-8"))
    else:
        print("error code:%d", resp.status_code)
    return session


def test_baidu():
    r = requests.get("https://www.baidu.com")
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        print(r.content[:500])
    else:
        print("error code:%d", r.status_code)


test_login()
params = {"country": 86,
          "cellphone": "15556925243",
          "password": "asdf1234",
          "captcha": "",
          "remember": 1,
          "platform": 3}
print(json.dumps(params))
print("************")
print(params)



# test_login()
# test_login()
