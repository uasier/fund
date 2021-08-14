import sqlite3  # 用来操作数据库

class sqlite3_handler:
    def __init__(self, dbpath) -> None:
        self.conn = sqlite3.connect(dbpath)
        # 获取cursor对象
        self.cursor = self.conn.cursor()
        # 首先确认是否创建了表结构
        try:
            create_tb_cmd='''
            CREATE TABLE IF NOT EXISTS FUND
            (ID TEXT,
            SHORTNAME TEXT,
            NAME TEXT,
            TYPE TEXT,
            LONGNAME TEXT);
            '''
            self.conn.execute(create_tb_cmd)
        except:
            raise("数据库创建异常")
        try:
            create_tb_cmd='''
            CREATE TABLE IF NOT EXISTS VALUE
            (ID TEXT,
            FSRQ TEXT,
            DWJZ TEXT,
            LJJZ TEXT,
            SDATE TEXT,
            ACTUALSYI TEXT,
            NAVTYPE TEXT,
            JZZZL TEXT,
            SGZT TEXT,
            SHZT TEXT,
            FHFCZ TEXT,
            FHFCBZ TEXT,
            DTYPE TEXT,
            FHSP TEXT,
            TIMESTAMP TEXT,
            J90JZ TEXT,
            J180JZ TEXT,
            J360JZ TEXT);
            '''
            self.conn.execute(create_tb_cmd)
        except:
            raise("数据库创建异常")
            
        # 把数据写进表中
        self.conn.commit()
        pass

    def update_fund(self, infos=[]):
        for i in infos:
            if not self.cursor.execute("select * from FUND where ID='{}'".format(i[0])).fetchall():
                self.cursor.execute(
                    '''INSERT INTO FUND values ("{}","{}","{}","{}","{}") '''.format(i[0], i[1], i[2], i[3], i[4])
                    )
        self.conn.commit()

        
    def update_fund_value(self, infos=[]):
        for i in infos:
            self.cursor.execute(
                '''INSERT INTO VALUE values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") '''. \
                format(i['ID'], i['FSRQ'], i['DWJZ'], i['LJJZ'], i['SDATE'], i['ACTUALSYI'], i['NAVTYPE'], i['JZZZL'], i['SGZT'], i['SHZT'], i['FHFCZ'], i['FHFCBZ'], i['DTYPE'], i['FHSP'], i['TIMESTAMP'], i['J90JZ'], i['J180JZ'], i['J360JZ'])
                )
        self.conn.commit()