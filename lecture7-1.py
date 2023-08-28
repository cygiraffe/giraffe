#구구단 프로그램(함수) 만들기

def GuGu(n):
    result = []
    i=1
    while i <10:
        result.append(n*i)
        i = i+1
    return result

print(GuGu(2))

#3과 5의 배수 합하기
result = 0
for n in range(1,1000):
    if n%3 ==0 or n%5==0:
        result += n
print(result)
    
#게시판 페이징하기
def GP(m,n):
    if m%n==0:
        return m//n
    else:
        return m//n +1  #(몫 더하기 1)
print(GP(5,10))

