from selenium import webdriver
from selenium.webdriver import Chrome
import os
import time
import pickle

damai_url = 'https://m.damai.cn/damai/home/index.html'
login_url = 'https://m.damai.cn/damai/minilogin/index.html?returnUrl=https%3A%2F%2Fm.damai.cn%2Fdamai%2Fmine%2Fmy%2Findex.html%3Fspm%3Da2o71.home.top.duserinfo&spm=a2o71.mydamai.0.0'
target_url = 'https://m.damai.cn/damai/detail/item.html?itemId=635455674312&spm=a2o71.home.recent_perform.ditem_0'

class Concert:
    def __init__(self):
        self.status = 0
        self.login_method = 1
        self.driver = webdriver.Chrome()
    def set_cookies(self):
        self.driver.get(login_url)
        print("###请扫码登陆###")
        time.sleep(30)
        print("###登陆成功###")
        pickle.dump(self.driver.get_cookie(), open('cookies.pkl', 'wb'))
        print("###保存成功！###")
        self.driver.get(target_url)
    def get_cookie(self):
        cookies = pickle.load(open('cookies.pkl', 'rb'))
        for cookie in cookies:
            print(cookie)
    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()
            else:
                self.driver.get(target_url)
                self.get_cookie()

if __name__ == '__main__':
    con = Concert()
    con.login()