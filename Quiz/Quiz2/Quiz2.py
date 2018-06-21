def fib(a,b) :
	print(a+b,b+(a+b),(a+b)+b+(a+b),b+(a+b)+(a+b)+b+(a+b))

first=input("Enter a Fibonacci number: ")
second=input("Enter the next Fibonacci number: ")
fib(int(first),int(second))