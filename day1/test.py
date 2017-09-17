#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie

import start
# 数字
a = 123+123
print a
import math
print math.pi
print math.sqrt(121)
import random
print random.random()
print random.choice([1, 3, 5, 7, 9, 11, 13])

# 调用start里面的方法，打印星号
start.pstart()
print "--------------------------------------------"
# 字符串 （从索引从 “0”开始）
s = 'spam'
print len(s)
# 分片提取  s[开始边界：截止边界]  注意：不包含截止边界
print s[1]
print s[-1]
print s[1:3]
print s[:3]
print s[1:]
print s[0:]
print s[:]
print s
print s.replace("pa", "xyz")

line = "aaa,bbb,cc,dd"
print line.split(",")
