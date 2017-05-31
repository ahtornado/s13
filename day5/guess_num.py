#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie
import random
retry_count = 0
real_num =random.randrange(10)
while retry_count < 3:
    guess_num=int (raw_input("Please guess the real num: "))
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

