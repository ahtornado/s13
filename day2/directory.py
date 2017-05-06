# _*_coding:utf_8_*_
# Author:Alvin.xie
#字典

E={'food':'spam','color':'pink','quantity':4}
print E
print E['food']
#字典排序
A={'a':1,'b':2,'c':3}
for key in sorted(A):
    print key,'=>',A[key]

D={'a':1,'b':2,'c':3}
print D


Ks=D.keys()
print Ks

Ks.sort()
print Ks

for key in Ks:
    print key,'=>',D[key]





