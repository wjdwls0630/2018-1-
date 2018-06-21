from math import cos,sin,exp,log
def math_box(val,func_name):
	if func_name=="cos" :
		a=cos(float(val))
	elif func_name=="sin" :
		a=sin(float(val))
	elif func_name=="exp" :
		a=exp(float(val))
	elif func_name=="log" :
		a=log(float(val))
	else :
		return
	return a
#print(math_box(24.5,"lsdfsd"))
# Do not modify below
func_name = input()
val = input()
result = math_box(val, func_name)
print( func_name+"("+val+") =", result)
