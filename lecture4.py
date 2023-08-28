현선 = True
찬영 = False
if not 2<3:
    print("현선이 보고 싶음")

else:
    #print("현선이 예쁨")
    pass
    # and : A and B 이면 A랑 B가 둘 다 True일 때에만 전체 식이 True가 됨
    # or: A or B 이면 A랑 B 둘 중 하나만 True 여도 전체 식이 True가 됨.
if 1 in [1,2,3]:
    #print("니가 가라 하와이")
    pass
else:
    print("부산을 가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass
elif not card:
    #print("택시를 타고가라")
# elif는 조건을 한번 더 주는거다.
    pass
else:
    #print("걸어가라")
    pass

score = 70
if score <=60:
    message = "success"
else:
    #message = "failure"
    pass
#print(message)

#조건부 표현식 (위의 식 덩어리와 같게 더 간단하게 식 쓸 수 있음)
#1. 성공일 때 조건 먼저 써준다.
#2. 조건식을 써준다.
message = "success" if score>=60 else "failure"
#print(message)

treehit=0
# while treehit <10:
    #treehit=treehit + 1
    #print("나무를 %d번 찍었습니다." % treehit)
    #if treehit == 10:
        #print("나무 넘어갑니다.")
#if 1:
    #print("a")

coffee=10
money=300
#while money:
    #print("돈을 받았으니 커피를 줍니다")
    #coffee = coffee-1
    #print("남은 커피의 양은 %d개입니다." %coffee)
    #if not coffee:
#        print("커피가 다 떨어짐 ㅅㄱ")
#        break

a=0
while a<10:
    a=a+1
    if a%2 ==0:
        continue
#continue : 코드가 더 이상 진행되지 않고 다시 while문 시작으로 돌아감.    
    print(a)

while True:
    print("ㅎㅎㅎ")