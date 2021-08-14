import requests
import json
import time
import copy


class fund_value():
    def __init__(self) -> None:
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://fund.eastmoney.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        }
    
    def change_time_2_int(self, str_time):
        timeArray = time.strptime(str_time, "%Y-%m-%d")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        return int(timestamp)
        
    def change_time_2_str(self, int_time):
        data_sj = time.localtime(int_time)
        time_str = time.strftime("%Y-%m-%d",data_sj)
        return time_str

    def get_fund_value(self, fundCode):
        self.params = (
            ('callback', "jQuery18309121914219352303_1628946635311"),
            ('fundCode', fundCode),
            ('pageIndex', '1'),
            ('pageSize', '100000'),
            ('startDate', ''),
            ('endDate', ''),
        )
        response = requests.get('http://api.fund.eastmoney.com/f10/lsjz', headers=self.headers, params=self.params)
        json_info = json.loads(response.text[41:-1])['Data']['LSJZList']
        res =[]
        i = len(json_info)
        j = 0
        timestamp = self.change_time_2_int(json_info[i - 1]['FSRQ']) - 86400
        while i > 0:
            i = i - 1
            timestamp = timestamp + 86400
            if timestamp == self.change_time_2_int(json_info[i]['FSRQ']):
                json_info[i]['TIMESTAMP'] = timestamp
                tmp =  copy.deepcopy(json_info[i])
            else:
                tmp = copy.deepcopy(json_info[i + 1])
                tmp['TIMESTAMP'] = timestamp
                tmp['FSRQ'] = self.change_time_2_str(timestamp)
                i = i + 1
            tmp['J90JZ'] = ""
            if j >= 90:
                tmp['J90JZ'] = res[j - 90]['LJJZ']
            tmp['J180JZ'] = ""
            if j >= 180:
                tmp['J180JZ'] = res[j - 180]['LJJZ']
            tmp['J360JZ'] = ""
            if j >= 360:
                tmp['J360JZ'] = res[j - 360]['LJJZ']
            tmp['ID'] = fundCode
            res.append(tmp)
            j = j + 1
        return res
