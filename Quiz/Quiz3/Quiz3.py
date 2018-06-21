"""숫자 두 개(a,b)를 입력받아 a<=범위<=b 인 범위 안에 랜덤한 숫자 n을 출력하고 코사인(n)를 구하라(?) """

from random import randrange
from math import cos
user=input()
a,b=user.split()
a=int(a)
b=int(b)
if a%2==0 :
    n=randrange(a,b+1,2)
else :
    n=randrange(a+1,b+1,2)

print(n)
print(cos(n))