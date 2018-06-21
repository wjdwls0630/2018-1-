#Text Practice
#Example
print("="*60)

user_input = input()
print ("Hello Goorm! Your input is " + user_input)

print("="*60)

#Problem 1
word=input("Enter a word:")
print(word[::-1])

print("="*60)

#Problem 2
name=input("Hello, what's your name?")
age=int(input("How old are you?"))
print(name,"is",age,"years old.")
print(name,"becomes",age+10,"years old after 10 years.")
print(name,"becomes 100 years old in",2018-(age+1)+100,end="")
print(".")

print("="*60)

#Problem 3
ID=input("주민등록번호 앞자리 : ")
year=ID[0:2]
month=ID[2:4]
day=ID[4:]
print("생일은","19"+year+"년",month+"월",day+"일")

print("="*60)

#Problem 4
apple=int(input("How many apples did you buy? "))
banana=int(input("How many banana did you buy? "))
melon=int(input("How many melon did you buy? "))
peach=int(input("How many peach did you buy? "))
grape=int(input("How many grape did you buy? "))
price_apple=3000
price_banana=2500
price_melon=10000
price_peach=5000
price_grape=4000
print("Price for apple :",apple,"*",price_apple,"=",apple*price_apple)
print("Price for banana :",banana,"*",price_banana,"=",banana*price_banana)
print("Price for melon :",melon,"*",price_melon,"=",melon*price_melon)
print("Price for peach :",peach,"*",price_peach,"=",peach*price_peach)
print("Price for grape :",grape,"*",price_grape,"=",grape*price_grape)
Total=apple*price_apple+banana*price_banana+melon*price_melon+peach*price_peach+grape*price_grape
print("Total price of your purchase :",Total)

print("="*60)

#Boolean Practice
print(True and not False)#True
#print(True and not false)
print(True or True and False)#True
print(not True or not False)#True
print(True and not 0)#True
print(52<52.3)#True
print(1+52<52.3)#False
print(4!=4.0)#둘의 문자타입이 다르지만 값이 같으므로 False
print(type(4)!=type(4.0))#둘의 문자타입이 다르므로 True

print("="*60)