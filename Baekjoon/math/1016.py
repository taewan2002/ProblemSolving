import sys
input = sys.stdin.readline

def solution(MIN,MAX):
    answer = MAX-MIN+1
    check = [False]*(MAX-MIN+1) # MIN~MAX까지의 수를 체크할 배열
    i=2
    while i*i <= MAX:
        square_number = i*i
        # MIN이 square_number의 배수가 아니라면, MIN이 속한 square_number의 첫번째 수를 구해준다.
        remain = 0 if MIN%square_number==0 else 1 
        j = MIN//square_number + remain
        while square_number*j <= MAX:
            # 이미 체크된 수는 넘어간다.
            if not check[square_number*j-MIN]:
                check[square_number*j-MIN]=True
                answer-=1
            j+=1
        i+=1        
    print(answer)
    

a,b = map(int,input().split())
solution(a,b)