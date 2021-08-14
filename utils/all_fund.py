import requests
import os
import json
import re


class all_fund():
    def __init__(self) -> None:
        self.headers = {
            'Referer': 'http://fund.eastmoney.com/js/fundcode_search.js',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        }

    def update_all_fund(self):
        fund_info = []
        self.params = (
        )
        response = requests.get('http://fund.eastmoney.com/js/fundcode_search.js', headers=self.headers, params=self.params)
        text = response.text[10 : (len(response.text))]
        text = text.split("]];")
        if len(text) != 2:
            return fund_info
        text = re.sub('"','',text[0])
        for fund in text.split("],["):
            fund_info.append(fund.split(","))
        return fund_info