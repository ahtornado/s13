# _*_coding:utf_8_*_
# Author:Alvin.xie
f = open('data.txt','w')
f.write('hello\n')
f.write('world\n')
f.close()

f = open('data.txt',"r")
print f

bytes=f.read()
print bytes
print bytes.split()

#类的创建
class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)

#类的实例创建使用
bob=Worker('Bob Smith',50000)
sue=Worker('sue Jone',60000)
print bob.lastName()

print sue.lastName()
print sue.giveRaise(0.1)
print sue.pay
