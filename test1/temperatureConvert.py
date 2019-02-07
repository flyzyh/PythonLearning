#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#输入
val = input("请输入带有温度表示符号的温度值（例如：32C表示32摄氏度，90F表示90华氏度):")
#如果字符串以C结尾（摄氏度），则转换为华氏度
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1]) +32
    print("转换后的温度为：%.2fF"%f)
#如果字符串以F结尾（华氏度），则转换为摄氏度
elif val[-1] in ['F', 'f']: 
    c = (float(val[0:-1]) -32) /1.8
    print("转换后的温度为：%.2fC"%c)
#其他情况则认为是输入错误
else:
    print("输入错误")
