#복습: 포매팅에서 %s는 문자열, %d는 정수
#함수 : 프로그래밍에서는 함수에서 입력값, 출력값이 필수로 필요한 건 아니다.
# 파이썬 함수의 구조
# def 함수명 (매개변수 (input))
    #<수행할 문장1>
    #<수행할 문장2>
    #return 리턴 값

def sum(a,b):
    result = a+b
    return result

print(sum(1,2))

#입력값이 없는 함수
#def say():
 #   return 'Hi'

#a=say()
#print(a)
#print(say())

#출력값이 없는 함수 = return값이 없다.
#def sum(a,b):
#    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

#print(sum(1,2))
#함수가 return 값이 있으면 print 해줬을 때 값이 나오고, reutrn 값이 없으면 print 했을 때 None이 찍힌다.
mylist = [1,2,3]
mylist.append(4)
print(mylist)

print(print("Hi"))

def sum_many(*args):   # args는 함수 iput값의 갯수를 제한하지 않고 몇개든 상관없게 짜고 싶을 때 쓴다.
    sum = 0
    for a in args:
        sum = sum +a
    return sum
print(sum_many(2,3,4))

#def print_kwargs(**kwargs):  # **은 딕셔너리에서 key에 대해서 *와 똑같은 원리로 적용되는 것.
 #   for k in kwargs.keys():
 #       #if(k=="name"):
 #       print("당신의 이름은:"+k)
#print(print_kwargs(name="int 조수", b=2))

#def say_myself(name, old, man=True):
    #print("나의 이름은 %s입니다." %name)
    #print("나이는 %d살입니다." %old)
    #if man:
     #   print("남자입니다.")
    #else:
    #    print("여자입니다.")
#say_myself("찬영", 29)

#변수의 효력범위
#a=1
#def vartest(a):
#    a = a+1
 #   return a

#print(vartest(a))
#print(a)

#a=1
#def vartest(a):
#    return a+1

#a=vartest(724)
#print(a)

#Lambda 함수
#add = lambda a,b: a+b
#result = add(3,4)
#print(result)

#hislist=[lambda a,b: a+b, lambda c,d:c/d]
#print(hislist[1](9,8))

#내장함수 입력 출력
#a= input()
#print(a)

#number = input("숫자를 입력하세요. ")
#print(number)

for i in range(10):
    print(i, end=" ")

f=open("새파일.txt", 'w', encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다\n" %i
    f.write(data)
print(" ")
f.close()

p=open("새파일.txt", 'r', encoding="UTF-8")
line = p.readline()
#readline은 첫줄부터 한줄을 읽어오는 함수
print(line)
p.close()

h = open("새파일2.txt", 'w')
h.close()