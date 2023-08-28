import mod1
print(mod1.add(8,90))

# 모듈(하나의 파이썬 파일) 안에서 함수 하나만 불러올 때
from mod1 import add
print(add(4,3))

# 폴더 안에서 모듈 하나 불러올 때
#from 큰폴더.작은폴더.모듈 import 함수
from cycoding1.lol1 import multi as mul
print(mul(7,6))

#f=open("없는파일",'r')

try:
    4/0
except ZeroDivisionError as e:
    print(e)

b=[1,2,3]
try:
    print(b[4])
except IndexError:
    print([5,6,7])