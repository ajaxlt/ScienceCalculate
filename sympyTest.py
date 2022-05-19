import numpy
from sympy import *
import numpy as np
x, y, z= symbols('x, y, z')

r1_3 = Rational(1, 3)  # 构造分数
print(r1_3, r1_3.evalf())  # 指定精度的数值解

'''符号函数转numpy函数'''
arc = np.pi / 3
expr = tan(x)
f = lambdify(x, expr, 'numpy')
print(f(arc))  # 数值解
print(expr.subs(x, pi/3))  # 符号解

'''化简'''
print(simplify(sin(x)**2 + cos(x)**2 + 2*x + 3*x))
print(expand((x + 1)**3))  # 展开

expr = x * y + x - 3 + 2*x**2 - z*x**2 + x**3
print(collect(expr, x)) #对x合并同类项

'''裂项'''
expr = 1 / (x * (x**2 + 1))
print(apart(expr))


'''微积分'''
print(diff(sec(x), x))
print(diff(exp(x*y*z), x))  #偏导数
print(integrate(exp(x*y*z), x))  #不定积分
print(integrate(sqrt(1-x**2), (x, -1, 1)))  #定积分

'''极限'''
print(limit((1+1/x)**x, x, +oo))
print(limit(1/x, x, 0, '-'))

'''泰勒展开'''
expr = sin(x)
print(expr.series(x, 0, 5))

'''解方程(用Eq构造等式)'''
eq = Eq(x**2 - 1, 0)
print(solveset(eq, x, domain=Reals))

f = symbols('f', cls=Function)
diffeq = Eq(f(x).diff(x, 2) - 2*f(x).diff(x, 1) + f(x), sin(x))
print(dsolve(diffeq, f(x)))


plot(x**3 + -x**2 + x)