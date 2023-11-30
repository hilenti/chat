import sqlite3
import os


class MyData:
    def __init__(self):
        db_file = os.path.join(os.path.split(os.getcwd())[0], 'data', 'user.db')

        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def change(self, a):
        self.cursor.execute(a)
        # 提交事务并关闭连接
        self.conn.commit()

    def getdata(self, a):
        self.cursor.execute(a)
        m = self.cursor.fetchall()
        return m


if __name__ == '__main__':
    my = MyData()
    my.change('create table if not exists friend(id varchar(20), username varchar(20), ip varchar(20))')
    my.conn.close()









