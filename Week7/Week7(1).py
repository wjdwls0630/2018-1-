#While-loop example 1
print("="*60)

rabbits=3
while rabbits>0 :
    print(rabbits)
    rabbits=rabbits-1

print("="*60)

#While-loop example 2

time=0
population =1000
growth_rate=0.21
while population<2000 :
    population=population+growth_rate*population
    print(round(population))
    time=time+1

print("It took {time} minutes for the bacteria to double.".format(time=time))
print("The final population was {population} bacteria.".format(population=round(population)))

print("="*60)

#Infinite-loop(임의로 break 걸어논 것)

time=0
population =1000
growth_rate=0.21
while True :
    if population <2000 :
        population = population + growth_rate * population
        print(round(population))
        time = time + 1
    else : break

print("="*60)

'''
#while True를 설정하면 break를 쓰지 않는 이상 infinite loop에 걸리고 while False를 설정하면 반복이 실행되지 않고 바로 종료된다.
#while True를 설정하고 break를 거는 방법도 있고 적절하게 조건문을 걸어서 while문을 쓰는 경우도 있다.
#if 문도 적절하게 쓰면 continue를 쓰지 않고도 제어할 수 있는 방법이 있다.
#취향 차이일 수도 있지만 교수님께서나 책에서나 continue와 break를 많이 쓰면 그 코드를 보는 사용자가 직관적으로 이해하지 못하기 때문에
# 많이 사용하면 그렇게 좋지는 않다고 한다.
#따라서 최대한 break와 continue 를 쓰지 않는 쪽으로 연습해보자.
'''


#break example(while)

#no break

#변수 초기화
s="C3H7"
i=0
while i<len(s) : #i가 문자 개수보다 작을 때 까지 반복한다.(for i in range(len(s))와 같은 횟수로 반복)(len(s)는 4이므로 i=0,1,2,3  4번 반복)
    if s[i].isdigit() : #s[i]를 봤을 때 숫자면 실행
        digit_index = i # 그 때 i를 변수 digit_index에 할당
        print(digit_index) # digit_index 출력
    i=i+1 #i에다 1을 더한 후 다시 처음으로 돌아간다

print("="*60)

#use break
#변수 초기화
s="C3H7"
i=0
while i<len(s) : #i가 문자 개수보다 작을 때 까지 반복한다.(for i in range(len(s))와 같은 횟수로 반복)(len(s)는 4이므로 i=0,1,2,3  4번 반복)
    if s[i].isdigit() : #s[i]를 봤을 때 숫자면 실행
        digit_index = i # 그 때 i를 변수 digit_index에 할당
        print(digit_index) # digit_index 출력
        break #숫자가 나오면 while 문 빠져나온다.
    i=i+1 # 숫자가 아니면 실행 - i에다 1을 더한 후 다시 처음으로 돌아간다

print("="*60)

#조건에 안 맞으면 처음으로 돌아가는 continue 1
#변수들이 초기화 되는 것이아니라 첫 수행문으로 다시 돌아가는 것이다.

#no continue

#변수 초기화
s="C3H7"
i=0
while i<len(s) : #i가 문자 개수보다 작을 때 까지 반복한다.(for i in range(len(s))와 같은 횟수로 반복)(len(s)는 4이므로 i=0,1,2,3  4번 반복)
    if s[i].isdigit() : #s[i]가 숫자면 실행
        pass #digit이어도 아무런 것을 수행하지 않고 넘어간다
    digit_index = i #다시 처음으로 돌아가거나 루프르 끊는 수행문이 없으니
                    # 그 다음 수행문인 digit_index에 그냥 i가 들어간다
    print(digit_index) # digit_index 출력
    i=i+1 # i에다 1을 더한 후 다시 처음으로 돌아가 다음 i를 진행한다.

#출력값은 0,1,2,3이 모두 나온다.

print("="*60)
#use continue

#변수 초기화
s="C3H7"
i=0
while i<len(s) : #i가 문자 개수보다 작을 때 까지 반복한다.(for i in range(len(s))와 같은 횟수로 반복)(len(s)는 4이므로 i=0,1,2,3  4번 반복)
    if s[i].isdigit() : #s[i]가 숫자면 실행
        i=i+1 # 다음 i로 진행해야하므로 더하고 continue를 넣어줘야한다.
        continue #숫자면 처음으로 돌아가 다시 실행
    digit_index = i # 숫자가 아닌 것이 나왔을 때 i를 변수 digit_index에 할당
    print(digit_index) # digit_index 출력
    i=i+1 # i에다 1을 더한 후 다시 처음으로 돌아가 다음 i를 진행한다.

#출력값은 문자열의 인덱스가 나온다
print("="*60)


