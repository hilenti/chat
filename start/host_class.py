import socket
import threading
import queue
import json  # json.dumps(some)打包   json.loads(some)解包
import os
import os.path
import sys
import functions


class ChatServer(threading.Thread):

    PORT = 9999  # 端口
    friends = []
    messages = queue.Queue()
    lock = threading.Lock()

    def __init__(self):         # 构造函数
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP = self.s.getsockname()[0]
        os.chdir(sys.path[0])
        my = functions.MyData()
        self.my_friends = list(my.getdata('select id from friend'))
        my.conn.close()

    def get_local_ip(self):
        try:
            self.s.connect(("8.8.8.8", 80))
            local_ip = self.s.getsockname()[0]
            return local_ip
        except socket.error:
            return "无法获取IP"

    def judge_friend(self, friend):
        if friend in self.my_friends:
            return True
        else:
            return False

    def add_friend(self, id_new, username, ip, check):
        if self.judge_friend(friend=id):
            return False
        else:
            my = functions.MyData()
            trun_funs = f"insert into friend(id, username, ip) values({id_new}, {username}, {ip})"
            my.change(trun_funs)
            my.conn.close()
            self.my_friends.append(id_new)

    def receive(self, conn, addr):
        user = conn.recv(1024)  # 用户名称
        information = user.decode()
        name = information['id']
        if name in self.my_friends:
            print(information['inform'])
        elif information['categories'] == 'add_friend':
            self.add_friend(information['id'], information['username'], information['ip'])


    def run(self):
        self.s.bind((self.IP, self.PORT))
        self.s.listen(5)
        while True:
            conn, addr = self.s.accept()
            t = threading.Thread(target=self.receive, args=(conn, addr))
            t.start()
        self.s.close()



