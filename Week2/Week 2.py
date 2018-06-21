#Python-provided function(파이썬 내장함수)
print("="*90)

print("Python-provided function(파이썬 내장함수)")

print(abs(-9.2))
print(pow(3,2))
print(round(4.3))
print(int(-4.3))
print(float(21))
print(min(2,3))
print(min(2,3,4))
print(min(2,-3,4,7,-5))
print(max(2,-3,4,7,-5))
print(max(2,-3,min(4,7),-5))
print(min(max(3,4), abs(-5)))
print(abs(min(4,6,max(2,8))))
print(round(max(5.572, 3.258)))

print("="*90)

#Function Practice 1
def sum(a,b):
	return a+b

# Define your other functions here
def multiple(a,b):
	return a*b
def subtract(a,b):
	return a-b
def multiply_three_numbers(a,b,c):
	x=multiple(a,b)
	y=multiple(x,c)
	return y

def add_and_multiply(a,b,c):
	return multiple(sum(a,b),c)

# Call your functions here
print("Function Practice 1")

print(sum(4,6))
print(multiple(4,6))
print(subtract(4,6))
print(multiply_three_numbers(4,6,2))
print(add_and_multiply(4,6,2))

print("="*90)

#Function Practice 2
def sum(a,b):
	return a+b

def multiple(a,b):
	return a*b

def subtract(a,b):
	return a-b

def add_and_multiply(a,b,c):
	return multiple(sum(a,b),c)

def add_min_numbers(a,b,c):
	return min(sum(a,b),sum(b,c),sum(a,c))

print("Function Practice 2")

print(add_and_multiply(4,6,2))
print(add_min_numbers(7,9,3))

print("="*90)
#FDR 1
def sub(a,b):
	return a-b
def abs_difference(a,b):
	"""
	(num,num) -> num
	Returns the absolute difference of the two numbers.

	>>>abs_difference(5,6)
	1
	>>>abs_difference(7,7)
	0
	>>>abs_difference(2.5,3.4)
	0.9
	"""
	return abs(sub(a,b))

print("FDR 1")

help(abs_difference)
print(abs_difference(-5,8))
print(abs_difference(21.45,20.8))
print(abs_difference(1+2j,3-4j))

print("="*90)

#FDR 2
def grade_average(A, B, C):
    """
    (num,num,num) -> num
    (num is between 0 and 100 inclusive (it means[0,100]))

    Returns the average of three numbers.

    >>>grade_average(20,40,60)
    40

    >>>grade_average(45,65,100)
    70
    """
    average_three_grades = (A + B + C) / 3
    return round(average_three_grades, 2)

print("FDR 2")

help(grade_average)
print(grade_average(45, 67, 48))

print("="*90)

