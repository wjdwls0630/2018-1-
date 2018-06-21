import random
print("가위바위보 게임을 만듭니다.")
while True :
    try :
        computer = random.randrange(0, 3)
        computer_result = {0: "바위", 1: "보", 2: "가위"}
        user=input("가위바위보! : ")
        user_result={"바위" : 0, "보" : 1, "가위" : 2}
        if computer==user_result.get(user) :
            print("컴퓨터가",computer_result.get(computer)+"를 냈습니다.\n비겼습니다.")
        else :
            if computer==int(user_result.get(user))+1 or computer==int(user_result.get(user))-2 :
                print("컴퓨터가", computer_result.get(computer) + "를 냈습니다.\n졌습니다.")
            else :
                print("컴퓨터가", computer_result.get(computer) + "를 냈습니다.\n이겼습니다!")
                break
    except :
        print("가위, 바위, 보 중에 하나만 입력하세요!")
        pass

