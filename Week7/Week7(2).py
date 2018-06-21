#for-loop

#보통 for 문
for i in range(1,10) :
    print(i)

print("="*60)

#이런 방법도 가능하다.
compound_elements=[["Li","F"],["Na","Cl"],["K","Br"]]
for [first,second] in compound_elements :
    print(first+second)
#리스트의 요소가 리스트이므로 리스트 형식을 만들어 first 와 second 에 리스트의 리스트요소를 할당 할 수도 있다.

print("="*60)
#parallel output
values= [4,10,3,8,-6]
for i in range(len(values)) : #len(values)는 5 range(5) 는 0부터 4까지 0,1,2,3,4  5번 반복
    print(i, values[i])

print("="*60)

#Nested loop(중첩루프)(ex. 2중루프, 3중루프 ... 그 이상은 안 쓰고 다른 방법을 찾는 것이 더 낫다)
positive=["Li","Na","K"]
negative=["F","Cl","Br"]
for i in positive : # 예를 들어 첫번째 요소 일 때
    for j in negative : #negative에 대한 중첩문 수행
        print(i+j) #첫번째 요소와 negative의 요소를 합친 것을 출력한다.

print("="*60)

#print multiplication table(구구단 태블릿 만들기 - 매우 중요)#내가 만든 방법
def print_multiplication(a) :
    print("%d단" %a)
    for i in range(1,10) :
        print(a*i)

#매우 중요
def print_multiplication_table(a): # 입력받은 a 값까지 출력
    #1단 ,2단 ..... a단 까지 출력하는 헤더(제목)부분
    for i in range(1,a+1) :
        print("%d단" %i,end="\t") #표를 정리하고 싶면
    print()#매우 중요 위의 print가 \t 인 상태로 남아있으므로 이 것이 없으면 다음 출력값은 같은 줄에 출력이 된다.
           # 문장을 다음줄로 넘기는 초기화 작업(\t를 없애는 과정)


    #구구단 태블릿 코드
    for i in range(1,10) : #1부터 9까지 반복(행이 1~9까지 9개가 됨)
        for j in range(1,a+1) : #1부터 사용자가 입력한 숫자까지 반복(열이 1~사용자가 입력한 숫자까지 만들어짐)
            print(j*i,end="\t") #i*1 i*2 ... i*a
        print()#\t 초기화 그리고 다음 행으로 i가 하나 넘어가는 것으로 다시 for i 밑 블록 수행

        #컴퓨터는 입력한 순서에 따라 명령을 수행하므로 잘 생각하고 만들어야 한다!


user_number1=int(input("몇단을 출력하시겠습니까? (1단부터 전체를 출력하려면 0을 입력하세요.) : "))
if user_number1 != 0 :
    print_multiplication(user_number1)
else :
    user_number2=int(input("그러면 몇 단 까지 출력하시겠습니까? : "))
    print_multiplication_table(user_number2)

print("="*60)

#교재 방법으로 하는 구구단 태블릿 (입력한 숫자의 행,열 숫자가 같은 표를 만들고, 행의 항목과 열의 항목을 곱하면 그 위치에 결과값을 입력하는 전형적인 구구단 표)
def print_table(n) :
    numbers=list(range(1,n+1))#range는 숫자 리스트를 생성하는 것이 아니라 그 입력한 값의 객체를 생성하는 것이므로 list화 시킨 후 저장해야한다.

    #헤더 부분 (1행 부분)
    for x in numbers :
        print("\t"+str(x),end=" ")# 처음에 0은 생략할 것이므로 처음 한칸 띄운후 시작 다음부터 계속 \t 한 간격으로 문자열이 입력됨
    print() #끝에 " " 부분으로 끝났으므로 이것이 없으면 다음 출력값이 같은 줄에 입력될 것이다. 다음 행으로 넘기는 작업 필수!
    #메인 부분
    for x in numbers :
        print(x,end=" ") #1열 부분 을 만드는 부분 착각하지 말아야할게 1열을 쓰고 넘어가는 것이 아니라 행을 먼저 쓰는 것
                         #ex 2  출력 후 2 4 6 8 10 ... 하고 또 다음 행으로 넘어가서 3 출력 후 3 6 9 12 ...
        for y in numbers :
            print('\t'+str(x*y),end=" ")
        print() #끝에  " " 부분으로 끝났으므로 초기화 필요 그리고 다시 돌아가 x에 1을 더한 후 다시 반복문 수행

print_table(6)

print("="*60)

#while문 을 for문으로도 만들 수 있다.(1)
#solution A
rabbits=3
for i in list(range(rabbits)) :
    print(rabbits)
    rabbits=rabbits-1

print("="*60)
#solution B
rabbits=3
time=range(rabbits)
for i in time :
    print(rabbits)
    rabbits=rabbits-1

'''
for i in range(rabbits)라고 하면 안되는 것이 반복문 중에 rabbits 의 객체가 변하므로 에러가 난다.
 변하지 않을 초기값을 넣거나 다른 변수에 초기값을 담고 그 변수로 for 문으로 돌린다
 이처럼 반복의 횟수를 조건문으로 잡은 while문은 쉽게 for문으로 바꿀 수 있다. 반대로 같은 방식으로 for문을 while문으로 바꿀수도 있다.
 하지만 경우에 따라서 for 문이 더 쉬운 경우가 있고  while문이 더 쉬운 경우가 있으므로 자기가 판단해서 적절하게 사용하면 된 다.

'''

print("="*60)

#for문의 continue와 break
#책의 예제는 while문을 통해서 해봤으니 다른 예제로 다시 break와 continue를 이해해보자.(Do it 파이썬 예제)

#break문(학교 예제)
time_default=10
time=time_default
population =1000
growth_rate=0.21
for i in range(time_default) :
    if population<2000 :
        population = population + growth_rate * population
        print(round(population))
        time=time-1
    else : break

print("It took {time} minutes for the bacteria to double.".format(time=time_default-time))
print("The final population was {population} bacteria.".format(population=round(population)))


'''
break문은 for 문에서는 잘 쓰이지 않는다.(for 문이 무한루프에 빠지는 경우는 없기 때문이다.)
 finite값을 iterate하는 거여서 if로 중간에 끊는 것 정도가 할 수 있는 것 같은데 굳이 그럴 필요가 있나 싶다(책의 예제 처럼 찾는 경우면 그럴 수도 있을 것 같다.)
물론 쓰고 싶거나 쓰일 상황이 있을 수 있는데 그러면 쓰면 된다. 중요한 건 for문에도 continue와 break를 할 수있다는 것이다.
'''


print("="*60)

#continue (1부터 10까지 홀수 만 출력하기)
for i in range(1,11) :
    if i%2 == 0 : continue #짝수면 처음으로 돌아간다. (밑에 print문 수행을 하지 않는다.)
    print(i)

print("="*60)

#continue 학생 점수 중 일정 점수 이상만 합격 문장 출력하기 (80점 이상이면 합격 문자 주기 )

#100명의 학생을 random모듈로 점수를 무작위로 생성해서 리스트에 담기
from random import randint
total=int(input("총 참석한 학생 수 :"))
total_pass=0
score_list=[]
for i in range(total) :
    score=randint(1,100)
    score_list.append(score)

print(score_list)

student_number=0
for a in score_list :
    student_number=student_number+1 #첫 시작 1번부터 해야되서 맨 처음 수행할 문장으로
    if a < 80 : continue #80점이하이면 다시 student_number에 1을 더한다.
    # 밑 for 블록은 80점 이상일 때만 실행된다
    print("{}번 학생 {}점으로 합격입니다. 축하합니다".format(student_number,score_list[student_number-1]))
    #파이썬 index는 0부터 시작하므로 1을 빼줘야 한다
    total_pass=total_pass+1 #80점이상이면 total_pass 에 1씩 더한다.

pass_rate=round((total_pass/total)*100 ,2)
print("합격률은 {pass_rate}%입니다".format(pass_rate=pass_rate))

print("="*60)

'''
리스트안에 for문을 작성하여 리스트 요소를 채울 수 있다.
 [표현식 for 항목1 in 반복 가능 객체1 if 조건1
       for 항목2 in 반복 가능 객체2 if 조건2
              ...
       for 항목n in 반복 가능 객체n if 조건n]
이런 식이다

 for 뒤에 :을 붙일 필요 없고 if 조건도 마찬가지로 안 붙여도 된다. 조금더 직관적으로 표현 가능해서 lambda 와 쓰는 의미가 비슷한 것 같다.
예를 들어 구구단의 모든 숫자들 중에 일의자리가 6인 숫자만 리스트에 담고싶으면 다음과 같이 하면 된다.
'''

number_six=[x*y for x in range(1,10)
            for y in range (1,10) if(x*y)%10==6]

from collections import OrderedDict
print(list(OrderedDict.fromkeys(number_six)))
