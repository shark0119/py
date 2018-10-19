import requests
import json

courseMap = {}

USER_NAME = '15556925243'
PWD = 'asdf1234'
LOGIN_URL = 'https://account.geekbang.org/account/ticket/login'
PRODUCTS_URL = 'https://time.geekbang.org/serv/v1/my/products/all'
ENCODING = "utf-8"


class Course:
    num = 0
    name = ""
    url = ""

    def __init__(self, num, name, url):
        self.num = num
        self.name = name
        self.url = url


class TakeCourse:
    _courseMap = {}
    _session = 0

    def login(self, user_name, pwd):
        login_params = {"country": 86,
                        "cellphone": user_name,
                        "password": pwd,
                        "captcha": "",
                        "remember": 1,
                        "platform": 3,
                        'appid': 1}
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
        self._session = requests.Session()
        resp = self._session.post(LOGIN_URL, data=json.dumps(login_params), headers=headers)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            print('login success:' + resp.content.decode(ENCODING))
        else:
            print("login failed. Error code:%d", resp.status_code)

    def list_courses(self):
        resp = self._session.post(PRODUCTS_URL)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            print('Obtain products success')
        else:
            print("Obtain products failed. Error code:", resp.status_code)
            return
        products_list = resp.content.decode(ENCODING)
        print(products_list.data[0].title)

    def take_course(self, course_no):
        pass


tc = TakeCourse()
tc.login(USER_NAME, PWD)
tc.list_courses()
