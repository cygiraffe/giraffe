a= ""
if a :
    print(a)
b = [1,2,3,4]
print(b)

a= [1,2,3]
b=a
print(a is b)
print (b)



c=[1,2,3]
d=c[:] # --> 값복사임
c.append(3)
print(c)
print(d)


e=[1,2,3]
from copy import copy
f=copy(e)
e[0]=9
print(e)
print(f)