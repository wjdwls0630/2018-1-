
a=int(input("Enter a number: "))
i=0
b=[]
while i <a :
	i=i+1
	if a%i ==0 :
		b.append(i)


if len(b)>2 :
	print("List of divisors: {}".format(b))
else :
	print("{} is a prime number".format(a))
		