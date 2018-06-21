import random
a=random.randrange(0, 3)
b={0: "바위", 1: "보", 2: "가위"}
c=input("가위바위보! : ")
d={"바위" : 0, "보" : 1, "가위" : 2}
if a==d.get(c) :
    print("컴퓨터가",b.get(a)+"를 냈습니다.\n비겼습니다.")
else :
    if a==int(d.get(c))+1 or a==int(d.get(c))-2 :
        print("컴퓨터가", b.get(a) + "를 냈습니다.\n졌습니다.")
    else :
        print("컴퓨터가", b.get(a) + "를 냈습니다.\n이겼습니다!")