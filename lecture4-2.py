#전형적인 for문
test_list = ['one', 'two','three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (b,c) in a:
    print(b+c)

#for문과 continue
marks = [90,25,67,45,80]
number = 0
for i in marks:
    number = number +1
    if i <60:
        continue
    #continue가 실행되면 아랫줄(print함수 줄)을 안 가고 다시 for문 시작부분으로 직행
    print("%d번 학생 축하합니다. 합격입니다." %number)

#range함수
sum = 0
for i in range(1,11):
    sum = sum+i

print(sum)

#구구단
a=10
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print(" ")

g=1
print(g==1)