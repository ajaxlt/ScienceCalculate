import scipy.integrate
from scipy import constants as C
from scipy import special as S
from scipy import integrate
import math

'''重要常数'''
print(C.pi)  # 圆周率
print(C.golden)  # 黄金分割
print(C.h)  # 普朗克常数

'''特殊函数'''
print(S.perm(5, 2))  # 排列数
print(S.comb(5, 2))  # 组合数
print(S.gamma(5))  # 伽马函数
print(S.sinc(0))  # sinc函数

'''定积分'''

'''一重积分'''
f_x = lambda x: math.sqrt(1-x**2)
ans, err = scipy.integrate.quad(f_x, -1, 1)
print(ans, err)

'''二重积分'''
f_xy = lambda x, y: x
x1, x2 = 0, 1
y1, y2 = lambda x: 0, lambda x: math.sqrt(1-x**2)
ans, err = scipy.integrate.dblquad(f_xy, x1, x2, y1, y2)
print(ans, err)




