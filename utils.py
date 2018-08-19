# by licw
# -*-coding=utf-8-*-
import requests

def get_data_from_sina(code):
    """
code: stock code, such as 000063
return: stock data list:
0: "华泰证券": 股票名字
1: "20.280": 今日开盘价
2: "20.250": 昨日收盘价
3: "20.340": 当前价格
4: "20.400": 今日最高价
5: "20.200": 今日最低价
6: "20.320": 竞买价，即“买一”报价
7: "20.340": 竞卖价，即“卖一”报价
8: "5737081": 成交的股票数（单位为“个”）
9: "116441306.000": 成交金额（单位为“元”）
10: "1200": “买一”申请 1200 股
11: "20.320": “买一”报价
12: "4900": “买二”申请 4900 股
13: "20.310": “买二”报价（以下依次类推）
14: "44300": 买三
15: "20.300": 买三
16: "30200": 买四
17: "20.290": 买四
18: "18900": 买五
19: "20.280": 买五
(20,21), (22,23), (24,25), (26,27), (28,29): 卖一，……，卖五
30: "2016-11-22": 日期
31: "09:48:11": 时间
    """

    base_url='http://hq.sinajs.cn/?format=text&list='
    if code.strip()<'600000':
        sina_url = base_url+'sz'+code
    else:
        sina_url = base_url+'sh'+code
    r = requests.get(sina_url)
    if r.status_code == 200:
        return r.text.strip('\n').split(',')
    else:
        return []

if __name__ == '__main__':
    code = '000063'
    data = get_data_from_sina(code)
    print data
