from utils import all_fund
from utils import sqlite3_handler
from utils import fund_value
import os

import yaml


if __name__ == "__main__":
    print("+++ 启动爬虫 +++")
    # if os.path.exists("res/fund.db"):
    #     os.system("rm -rf res/fund.db")
    all_fund_ins = all_fund()
    sqlite3_handler_ins = sqlite3_handler(dbpath="res/fund.db")
    fund_value_ins = fund_value()
    infos = all_fund_ins.update_all_fund()
    sqlite3_handler_ins.update_fund(infos=infos)
    for info in infos:
        print(info[0])
        fund_value_info = fund_value_ins.get_fund_value(info[0])
        sqlite3_handler_ins.update_fund_value(infos=fund_value_info)
