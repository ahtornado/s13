#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie
import random
retry_count = 0
#�������һ��10���ڵ���
real_num =random.randrange(10)
while retry_count < 3:
    #ȥ���ո�ͻس�
    guess_num=raw_input("Please guess the real num: ").strip()
    #�жϳ����Ƿ�Ϊ 0
    if len(guess_num) == 0:
        continue
    #�ж��Ƿ�Ϊ����
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print "You need input num"
        continue
    if guess_num > real_num:
        print "Wrong ! you need try smaller!"
    elif guess_num < real_num:
        print "Wrong ! you need try bigger!"
    else:
        print "Congratulations! you successful!"
        break
    retry_count +=1
else:
    print "The real num is :", real_num

