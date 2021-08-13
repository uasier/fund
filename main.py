from utils import all_fund
from utils import sqlite3_handler

import yaml

if __name__ == "__main__":
    all_fund_ins = all_fund()
    sqlite3_handler_ins = sqlite3_handler(dbpath="res/db.db")
    for i in range(20):
        print(i)
        infos = all_fund_ins.update_all_fund(page=1, num=50000)
        sqlite3_handler_ins.update_fund(infos=infos)
        exit()
