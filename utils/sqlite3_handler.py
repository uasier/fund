import sqlite3  # 用来操作数据库

class sqlite3_handler:
    def __init__(self, dbpath) -> None:
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor() #获取cursor对象
        pass

    def update_fund(self, infos=[]):
        # 首先确认是否创建了表结构
        try:
            create_tb_cmd='''
            CREATE TABLE IF NOT EXISTS FUND
            (ID TEXT,
            NAME TEXT,
            SHORTNAME TEXT,
            COMPANYCODE TEXT,
            TYPE TEXT,
            ESTABLISHED TEXT,
            MANAGER TEXT,
            PURCHASE TEXT,
            COMPANY TEXT);
            '''
            #主要就是上面的语句
            self.conn.execute(create_tb_cmd)
        except:
            print("数据库创建异常")
        # 第二步获取最新的表数据
        for i in infos:
            print(self.cursor.execute("select * from FUND where ID='{}'".format(i[0])).fetchall())
            if not self.cursor.execute("select * from FUND where ID='{}'".format(i[0])).fetchall():
                self.cursor.execute(
                    '''INSERT INTO FUND values ("{}","{}","{}","{}","{}","{}","{}","{}","{}") '''.format(i[0], i[1], i[2], i[3], i[4], i[6], i[8], i[9], i[13])
                    )
        # 把数据写进表中
        self.conn.commit()