#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019-2020 LX
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

import random
# 获取一个1-10的随机整数：
answer = random.randint(1,10)
lucky_num = str(answer)
print('==========Find your lucky number==========')
shuru = str(input('Input a number between 1 to 10 and press Enter:'))
check = shuru.isdigit()
# 检测输入字符是否为数字：
while check == 0:
        shuru = str(input('Please input a Arabic numeral:'))
        check = shuru.isdigit()
else :
        Num = int(shuru)
        if Num == answer:
                print('1 shoot 1 kill,', lucky_num, 'is your lucky number!')
        else:
                # 执行数字大小比较：
                while Num != answer:
                        if Num > answer:
                                shuru = input('Wrong, input a smaller number:')
                        else:
                                shuru = input('Wrong, input a bigger number:')
                        Num = int(shuru)
                print('Okey,', lucky_num, 'is your lucky number!' )