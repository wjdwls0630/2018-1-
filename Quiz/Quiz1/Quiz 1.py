def max_first(a,b,c) :
    return max(a,b,c)==a

number=input("6자리 숫자 : ")
first=int(number[:2])
second=int(number[2:4])
third=int(number[4:])
print(max_first(first,second,third))

