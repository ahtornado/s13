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

for c in "spam":
    print c.upper()
#迭代和优化,，使用解析表达式创建一个列表
squares=[x**2 for x in [1,2,3,4,5]]
print squares

#等价于下面的，但是下面速度比较慢
squares1=[]
for x in [1,2,3,4,5]:
    squares1.append(x**2)
print squares1







