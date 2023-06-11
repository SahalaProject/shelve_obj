import shelve
from ctypes import *


#################待 持久化对象 写的对象#################
class UserInfo(Structure):
    __fields__ = [
        ('coler', c_char)
    ]


u = UserInfo(coler=b'blue')
print(u.coler)


class Globle:

    def __init__(self, name):
        self.name = name
        self.user = u

    def init(self):
        self.age = 12


##################################


with shelve.open('test') as file:
    file['Globle'] = Globle(name=12)

with shelve.open('test') as file:
    file['step'] = {'data': {'json': "{'struct_userinfo': UserInfo(coler=b'black')}"}}

with shelve.open('test') as file:
    file['UserInfo'] = u

with shelve.open('test') as file:
    data = file['Globle']
    print(data.name)
