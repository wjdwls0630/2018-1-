user_input=int(input("몇 줄을 출력하시겠습니까? : "))

for x in range(1,user_input*2,2) :
    if x<=user_input:
        print((" " * ((user_input * 2 - 3 - x) // 2)) + ("*" * x))
    else:
        print((" " * (((user_input*2)-(user_input * 2 + 3 - x)) // 2)) + ("*" * (user_input*2-x)))


#for문을 한번 사용하여 다이아 모양을 만들어라
