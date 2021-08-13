import requests
import os
import json
import re


class all_fund():
    def __init__(self) -> None:
        self.headers = {
            'Referer': 'http://fund.eastmoney.com/data/FundNewIssue.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        }

    def update_all_fund(self, page=1, num=20):
        fund_info = []
        self.params = (
            ('t', 'xcln'),
            ('sort', 'jzrgq,desc'),
            ('page', '{},{}'.format(page, num)),
        )
        response = requests.get('http://fund.eastmoney.com/data/FundNewIssue.aspx', headers=self.headers, params=self.params)
        text = response.text[25 : (len(response.text))]
        text = text.split("]],record")
        if len(text) != 2:
            return fund_info
        text = re.sub('"','',text[0])
        for fund in text.split("],["):
            fund_info.append(fund.split(","))
        return fund_info