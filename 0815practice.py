#1번
def is_odd(number):
    if number%2==0:
        return True
    else:
        return False
    
print(is_odd(2))

#4번
# 답 : 3번


#5번
f1=open("test0815.txt", 'w')
f1.write("Life is too short\nyou need python")
f1.close()

f2=open("test0815.txt", 'r')
print(f2.read())

#6번
#user_input=input("저장할 내용을 입력하세용:")
#f=open('test0815.txt', 'a')
#f.write(user_input)
#f.write('\n')
#f.close()

#7번
f= open('test0815.txt', 'r')
body = f.read()
f.close()

body = body.replace('python', 'java')

f= open("test0815.txt", 'w')
f.write(body)
f.close()

#262쪽
#1번
class Calculator:
    def __init__(self):
        self.value=0

    def add(self,val):
        self.value+= val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

#2번
class maxlimit(UpgradeCalculator):
    def add(self, val):
        super().add(val)
        if self.value >100:
            self.value = 100

cal=maxlimit()
cal.add(50)
cal.add(60)
print(cal.value)

#7번
a= [-8,2,7,5,-3,5,0,1]
b= max(a)
c=min(a)
print(b+c)

#8번
b=17/3
c=round(b,4)
print(c)