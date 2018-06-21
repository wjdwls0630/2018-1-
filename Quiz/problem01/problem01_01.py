def average_grade(a,b,c) : #average_grade라는 함수를 정의 , 매개변수(parameter)는 a,b,c 세 개 -> 입력할 때 세 개 인자를 무조건 써야함

    if 0<=a<=100 and 0<=b<=100 and 0<=c<=100 : # 한 개라도 False일시 else 문으로 이동, 조건 세 개가 모두 참 일시 실행

        result=(a+b+c)/3 # if의 block문 입력받은 인자(argument)의 평균 값(value)를
                         # result라는 지역변수(local variable)에 할당(assign)

    else : #입력받은 인자가 한개라도 [0,100] 사이의 범위를 벗어나면 실행

        result="잘못된 범위를 입력하셨습니다." #result 변수에 "잘못된 범위를 입력하셨습니다." 라는 문자열(type : str)을 할당(assign)

    return result #result(지역변수) 값 반환(return)


print(average_grade(50,47,65))
print(average_grade(101,9,4))

result=3 #average_grade의 블록 안에 있는 result는 함수 안에서만 적용 (지역변수 이므로)
         #  실행시켜보면 알 수 있듯이 함수 밖에서 result는 다른 값을 가지는걸 확인 가능
print(result)