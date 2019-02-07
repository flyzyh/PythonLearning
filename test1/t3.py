# -*- coding: utf-8 -*-
age = 9
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

height = 1.75
weight = 80.5
bmi = weight / (height * height)
print('bmi is ',bmi)
if bmi < 18.5:
    print('体重过轻')
elif bmi < 25:
    print('体重正常')
elif bmi < 28:
    print('体重肥胖')
elif bmi < 32:
    print('严重肥胖')
