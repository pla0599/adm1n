#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019-2020 LX
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

import random
answer = random.randint(1,10)
print('==========Find your lucky number==========')
shuru = str(input('Input a number between 1 to 10 and press Enter:'))
check = shuru.isdigit()
while check == 0:
        shuru = str(input('Please input a Arabic numeral:'))
        check = shuru.isdigit()
else :
        Num = int(shuru)
        lucky_num = str(answer)
        if Num == answer:
                print('1 shoot 1 kill,', lucky_num, 'is your lucky number!')
        else:
                while Num != answer:
                        if Num > answer:
                                shuru = input('Wrong, input a smaller number:')
                        else:
                                shuru = input('Wrong, input a bigger number:')
                        Num = int(shuru)
                print('Okey,', lucky_num, 'is your lucky number!' )
