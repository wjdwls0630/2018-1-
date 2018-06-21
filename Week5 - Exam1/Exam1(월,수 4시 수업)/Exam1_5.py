
from math import pi,sqrt,exp


mu=input("Enter mu: ")
sigma=input("Enter sigma: ")
x=input("Enter x: ")

def normal (x,mu,sigma):
    a=1/sqrt(2*pi*pow(sigma,2))
    b=pow((x-mu),2)
    c=2*pow(sigma,2)
    d=exp(-(b/c))
    return a*d

print("p(x) =",round(normal(float(x),float(mu),float(sigma)),3))