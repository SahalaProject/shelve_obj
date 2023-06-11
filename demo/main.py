import json
from ctypes import *
import shelve


############## 持久化对象 写的对象的初始定义 #################
class UserInfo(Structure):
    __fields__ = [
        ('cooler', c_char)
    ]


class Globle:

    def __init__(self, name):
        # self.name = name
        pass

    def init(self):
        self.age = 12


##################################

# 读 对象持久化
with shelve.open('test') as file:
    g = file.get('Globle')
    step = file.get('step')
    u_i = file.get('UserInfo')
    print(g.name)
    print(step)
    print(u_i.coler)

g.name = 'gaga'
print(g.name)
print(g.init())
print(g.age)
print('对象-》结构体-》value：', g.user.coler)

step_json = step.get('data', {}).get('json', '')
print(type(step_json))
res = eval(step_json)
struct_userinfo = res.get('struct_userinfo')
print(struct_userinfo.coler)

# 结果写对象持久化
with shelve.open('result') as file:
    file['result'] = struct_userinfo.coler
