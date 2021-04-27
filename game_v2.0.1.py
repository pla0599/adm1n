#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2019-2021 LX
# All Rights Reserved.
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
import random
answer = random.randint(1, 10)
lucky_num = int(answer)
print('============Find your lucky number============')
shuru = str(input('Input a number between 1 to 10 and press Enter:'))
check = shuru.isdigit()
if check == True:
    if int(shuru) == answer:
        print('1 shoot 1 kill,', lucky_num, 'is your lucky number!')
    else:
        while check == False:
            shuru = str(input('Please input a Arabic number:'))
            check = shuru.isdigit()
            continue
        else:
            while str(shuru) != str(answer):
                if check == True:
                    shuru = int(shuru)
                    if shuru > answer:
                        shuru = input('Wrong, input a smaller number:')
                        check = shuru.isdigit()
                        if check != False:
                            continue
                        else:
                            shuru = input('Please input a Arabic number:')
                            check = shuru.isdigit()
                            if check != False:
                                continue
                    else:
                        shuru = input('Wrong, input a bigger number:')
                        check = shuru.isdigit()
                        if check != False:
                            continue
                        else:
                            shuru = input('Please input a Arabic number:')
                            check = shuru.isdigit()
                            if check != False:
                                continue
                else:
                    shuru = input('Please input a Arabic number:')
                    check = shuru.isdigit()
                    if check != False:
                        continue
            else:
                print('Okey,', lucky_num, 'is your lucky number!')
else:
    while check == False:
        shuru = str(input('Please input a Arabic number:'))
        check = shuru.isdigit()
        continue
    else:
        while str(shuru) != str(answer):
            if check == True:
                shuru = int(shuru)
                if shuru > answer:
                    shuru = input('Wrong, input a smaller number:')
                    check = shuru.isdigit()
                    if check != False:
                        continue
                    else:
                        shuru = input('Please input a Arabic number:')
                        check = shuru.isdigit()
                        if check != False:
                            continue
                else:
                    shuru = input('Wrong, input a bigger number:')
                    check = shuru.isdigit()
                    if check != False:
                        continue
                    else:
                        shuru = input('Please input a Arabic number:')
                        check = shuru.isdigit()
                        if check != False:
                            continue
            else:
                shuru = input('Please input a Arabic number:')
                check = shuru.isdigit()
                if check != False:
                    continue
        else:
            print('Okey,', lucky_num, 'is your lucky number!')