def pow_div(x,y,z) :
	return pow(x,y)/z
def mult_module(x,y,z):
	return (x*y)%z
def add_idiv(x,y,z):
	return (x+y)//z
def mult_pow(x,y,z) :
	return pow(x*y,z)
	
# Do not modify below
x = float(input())
y = float(input())
z = float(input())

print(pow_div(x, y, z))
print(mult_module(x, y, z))
print(add_idiv(x, y, z))
print(mult_pow(x, y, z))