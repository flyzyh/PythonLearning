#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def check_version():
    v = sys.version_info
    print('Major:', v.major, 'Minor:', v.minor, 'Micro:', v.micro)
    if v.major == 3 and v.minor >= 5:
        print('Your current python is %d.%d.%d. Success ' % (v.major, v.minor, v.micro))
        return
    print('Your current python is %d.%d. Please use Python 3.6.' % (v.major, v.minor))
    exit(1)


# check_version()

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('%2d-%02d' % (3456, 1234))
print('%.3f' % 3.1415926)
s1 = 72
s2 = 85
r = (85-72)/72
print('成绩提高了%.2f %%' % r)
print('Hello, {0}, 成绩提升了 {1:.3f}%'.format('小明', r))
