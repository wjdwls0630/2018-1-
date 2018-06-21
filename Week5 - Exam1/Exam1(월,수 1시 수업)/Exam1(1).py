def convert1(number1) :
    number2=10-number1
    return number2

def Num_to_MorseCode(number1) :

    if number1<=5 :
        result=("*"*number1)+("_"*(convert1(number1)-5))
    elif number1<=10 :
        result=("_"*number1-5)+("*"*convert1(number1))
    return result


input_number=input("3자리 숫자 입력하시오 : ")

if 100<=int(input_number)<=999 :
    a = int(input_number[0])
    b = int(input_number[1])
    c = int(input_number[2])
    print(Num_to_MorseCode(a),Num_to_MorseCode(b),Num_to_MorseCode(c))
else : print("Error: Invalid Range")

