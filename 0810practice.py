#1번
def is_odd(number):
    if number%2==0:
        return True
    else:
        return False

#2번
def avg_numbers(*args):
    result=0
    for i in args:
        result +=i
    return result/len(args)

print(avg_numbers(1,2))

#3번
input1= input("첫번째 숫자를 입력하세요")
input2= input("두번째 숫자를 입력하세요")
input1=int(input1)
input2=int(input2)
total = input1+input2
print("두 수의 합은 %s입니다" % total)
