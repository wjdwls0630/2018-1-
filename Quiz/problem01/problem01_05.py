def convert_computer(a) : #random 모듈 randrange함수로 만든 컴퓨터의 난수를 묵, 찌 , 빠 로 변환해주는 함수
    if a==0 :
        convert_computer_input="묵"
    elif a==1 :
        convert_computer_input="빠"
    else :
        convert_computer_input="찌"
    return convert_computer_input
# 컴퓨터가 생성한 난수가 0이면 묵 1이면 빠 2이면 찌 -> 숫자가 +1 큰 쪽이 이기는 순서 (예외 : 가위는 2이고 묵이면 0이므로 이 경우는 따로 조건을 만들어야함)

def convert_user(b) : #사용자가 입력한 묵, 찌, 빠를 숫자 0,1,2로 변환해주는 함수
    if b=="묵" :
        convert_user_input=0
    elif b=="빠" :
        convert_user_input=1
    else :
        convert_user_input=2
    return convert_user_input
#사용자가 입력한 문자가 묵이면 0 빠이면 1 찌이면 2 -> 숫자가 +1 큰 쪽이 이기는 순서 (예외 : 가위는 2이고 묵이면 0이므로 이 경우는 따로 조건을 만들어야함)
#또한 컴퓨터와 유저의 값을 같게해야 나중에 조건을 짤 때 안 헷갈림

def result_game(user_input) : #컴퓨터와 사용자의 숫자를 보고 비교하여 승부의 결과를 출력하는 함수

    if computer_input==convert_user(user_input) : #같은 값을 가지면 둘 다 같은 걸 낸 것이므로 비긴다.
        result = "비겼습니다."

    elif computer_input==convert_user(user_input)+1 or computer_input==convert_user(user_input)-2 :
    #숫자가 +1 큰 쪽이 이기는데 컴퓨터가 큰 것으로 조건을 생성 -> 컴퓨터가 이기는 상황
    # 예외로 가위는 2이고 묵이면 0이므로 사용자가 가위(2)를 냈을 때 컴퓨터가 묵(0)이어야 하므로 -2를 해주는 조건 추가
        result = "졌습니다."

    else : #나머지 모든 경우에서는 이기는 경우 밖에 없음
        result = "이겼습니다."

    return result #문자열을 할당한 지역변수 result 를 반환(출력,리턴)


from random import randrange #random 모듈에서 randrange함수만 불러온다

computer_input=randrange(0,3) #[0,3) 인 범위에서 정수인 값을 random으로 불러온다

user_input=input("[묵, 찌, 빠] 중 하나를 입력하세요 : ")
print("컴퓨터 입력 :",convert_computer(computer_input))

print(result_game(user_input))

#묵 , 찌 , 빠가 아닌 다른 것을 입력했을 때 비겼습니다 가 나오는 이유는 위에 유저와 컴퓨터의 값을 convert하는 함수에서
#else 로 모든 경우를 다 포함 하므로 둘다 2라는 값을 가진다 그러므로 둘의 숫자가 같으니까 result_game에 if조건문을 만족하므로
#비겼습니다가 나오는 것
#묵, 찌 , 빠 말고 다른 것을 입력하면 오류가 나거나 다시 입력하라고 하는 것 아직 안해도 되는 것이므로 생략


