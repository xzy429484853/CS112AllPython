from sympy import *


t= symbols('t')

x = Function('x')(t)

diffeq = Eq(10. * x.diff(t,t) - 7.348 * x.diff(t) + 1.325 * x)

yxdd = dsolve(diffeq,x)

print(yxdd)