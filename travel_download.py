# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 下午10:20
# @Author  : xiaotian
# @Email   : baigg2013@163.com
# @File    : travel_download.py
# @Software: PyCharm
import random
import time

import bs4
import requests


class DunHuang:
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3",
        "Cookie": "mfw_uuid=5dd27340-0f45-ff42-1a3a-0744fe7a90b5; "
                  "oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22"
                  "%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222019-11-18+18%3A32%3A32%22%3B%7D; __mfwc=direct; "
                  "uva=s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1574073153%3Bs%3A10%3A%22last_refer%22%3Bs%3A24"
                  "%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; "
                  "__mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1574073153%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A"
                  "%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; "
                  "__mfwuuid=5dd27340-0f45-ff42-1a3a-0744fe7a90b5; "
                  "UM_distinctid=16e7e123fef4e1-02c4731bcb3d0e-14291003-1fa400-16e7e123ff06e1; "
                  "__mfwa=1574073154592.41083.3.1574077524550.1574171715575; __mfwlv=1574171715; __mfwvn=2; "
                  "__jsluid_h=9ef4c7cb671f9afa2aad419a179a1647; __omc_chl=; __omc_r=; "
                  "PHPSESSID=clmadiuq6sha7va0elf73rlam5; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1574073155,"
                  "1574171716,1574173100; CNZZDATA30065558=cnzz_eid%3D2060055507-1574071549-https%253A%252F%252Fwww"
                  ".mafengwo.cn%252F%26ntime%3D1574173216; __mfwb=7fcff7a4dc01.16.direct; __mfwlt=1574174200; "
                  "Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1574174201; "
                  "__jsl_clearance=1574174686.567|0|ieQmVq2XUoUQcN%2F3QLUUQ5Q5DN0%3D",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 "
                      "Safari/537.36 "
    }

    def __init__(self):
        pass

    # 获取html信息
    def get_url_text(self, url):
        resp_text = ""
        try:
            resp = requests.get(url, headers=self.header)
            # resp.encoding = "utf-8"
            resp_text = resp.text
            # print(resp_text)
        except Exception as e:
            print("dowdload url failed!")
        else:
            return resp_text

    def get_url_detail(self, url):
        html_str = self.get_url_text(url)
        # print(html_str)
        url_list = self.handle_url_detail(html_str)

        return url_list

    def handle_url_detail(self, html_str):
        soup = bs4.BeautifulSoup(html_str, features="lxml")
        post_cover_all = soup.find_all('div', class_="post-cover")
        # print(post_cover_all)
        url_list = []
        for i in post_cover_all:
            a = i.find('a')
            # print(a.get("href"))
            url_list.append("http://www.mafengwo.cn" + a.get("href"))
        return url_list
        # print(i.split("a href=")[-1])

    def handle_real_url(self):
        pass

    def main(self):
        url_base = "http://www.mafengwo.cn/yj/10240/1-0-{}.html"
        # url = url_base.format(str(1))
        # self.get_url_detail(url)
        with open("url.list", 'w+') as url_all_file:
            for i in range(1, 183):
                url = url_base.format(str(i))
                time.sleep(random.randint(1, 10))
                url_list = self.get_url_detail(url)
                for url in url_list:
                    url_all_file.write(url + "\n")
                    print(url)

    def download_img(self):
        pass


if __name__ == '__main__':
    hhh = DunHuang()
    hhh.main()
    # print(hhhh)
