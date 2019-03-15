from sympy import *

t= symbols('t')
x = Function('x')(t)

diffeq = Eq(10. * x.diff(t,t) - 7.3 * x.diff(t) + 1.1 * x)
yxdd = dsolve(diffeq)

print(yxdd)
print("")
pprint(yxdd)
