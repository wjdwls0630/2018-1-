# Your code here
def subtract_and_multiply(a,b,c):
	return (a-b)*c

def convert_to_celsius(F):
	C=(F-32)*5/9
	return C
	

# Do not modify below
(a,b,c) = input().split()
a = int(a)
b = int(b)
c = int(c)
print(subtract_and_multiply(a,b,c))
print(convert_to_celsius(a))