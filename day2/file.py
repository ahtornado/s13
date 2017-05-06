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