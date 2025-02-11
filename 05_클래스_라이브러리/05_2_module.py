# import 모듈 이름
# from 모듈_이름 import 모듈_함수

import mod1
print(mod1.__name__) # mod1
print(mod1.add(3, 4))

from mod1 import add
print(add(3,4))

from mod1 import add, sub
print(add(3,4), sub(3,4))

from mod1 import *
print(sub(3,4))

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))


# 다른 디렉토리에 있는 모듈 불러오기
# sys.path.append("/Users/hyewon/Desktop/딥러닝/파이썬/python-practice/mod3.py")
# import mod3
# print(mod3.add(3,4))