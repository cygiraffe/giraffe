#a=1
#def vartest(a):
#    a= a+1
#vartest(a)

#a=10
#def func():
 #   global a
  #  a=50
   # print(f"2.{a}")
    #return a+100

#print(f"1.{a}")
#print(f"3.{func()}")

#클래스를 쓰는 방법
#1. Class를 입력하고, 2. 대문자로 시작하는 클래스의 이름을 작성 3. 안에 들어갈 함수와 변수 설정

class Fourcal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
            
a=Fourcal(4,2)
a.setdata(4,2)
#클래스에서는 객체(여기서는 a)가 변수 self의 자리에 디폴트로 들어간다. 
print(a.first)
print(a.second)
print(a.add())

#클래스의 상속
class MoreFourcal(Fourcal):
    third =5
    fourth =6
    def pow(self):
        result = self.first**self.second  # **은 제곱이다.
        return result
 
a=MoreFourcal(4,2)
print(a.add())
print(a.pow())
print(a.third)