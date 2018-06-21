from math import sin,cos,pi,radians

print(sin(pi/6))
r=float(input("r :"))
a=float(input("alpha :"))
b=float(input("beta :"))
x=round(r*sin(radians(b))*cos(radians(a)),2)
y=round(r*sin(radians(b))*sin(radians(a)),2)
z=round(r*cos(radians(b)),2)
print("(x,y,z) =",(x, y, z))