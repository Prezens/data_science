# Calculations with strict and without strict accounting of errors


import math

# 1)

a = 187.7
b = 66.6
c = 72.3

Da = 0.04
Db = 0.02
Dc = 0.03

X = (math.sqrt(a) * b) / c

da = Da / a
db = Db / b
dc = Dc / c

dX = 0.5 * da + db + dc
DX = X * dX

print('X:', X)
print('dX:', dX)
print('DX:', DX)


# # 2)

# a = 11.8
# b = 7.4
# m = 5.82
# c = 26.7
# d = 11.234
#
# Da = 0.02
# Db = 0.03
# Dm = 0.005
# Dc = 0.03
# Dd = 0.004
#
# X = ((m ** 3) * (a + b)) / (c - d)
#
# da = Da / a
# db = Db / b
# dm = Dm / m
# dc = Dc / c
# dd = Dd / d
#
# dX = (3 * dm) + (((a * Da) + (b * Db)) / (a + b)) + (((c * Dc) + (d * Dd)) / (c - d))
# DX = X * dX
#
# print('X:', X)
# print('dX:', dX)
# print('DX:', DX)


# # 3)

# a = 9.05
# b = 3.244
# h = 20.18
#
# M = (((a + b) * (h ** 3)) / 4) + ((a + b) * h) / 12
#
# print('M: %.2f' % M)
