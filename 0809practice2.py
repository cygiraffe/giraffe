result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#3번
i=0
while True:
    i+=1
    if i>=6:break
    print("*"*i)

#4번
#for i in range(1,101):
 #   print(i)

#5번:
A=[70,60,55,75,95,90,80,80,85,100]
total =0
for score in A:
    total += score
average = total/len(A)
print(average)

#6번
numbers =[1,2,3,4,5]
result = []
for n in numbers:
    if n%2==1:
        result.append(n*2)

 #6. 리스트 내포해서 동일 표현 만들기
numbers =[1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print (result)