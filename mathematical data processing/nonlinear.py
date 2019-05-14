# Methods for solving nonlinear equations


import math

# e-x – 2,6x + 4,3 = 0

f = lambda x: math.e ** (-x) - 2.6 * x + 4.3

a1 = 0
b1 = 5
e = 0.00001

x0 = a1
x1 = b1

y0 = f(x0)
y1 = f(x1)

k = 0
de = 0

while True:
    k += 1
    d = x1 - x0
    z = x1 - ((y1 * d) / (y1 - y0))

    de = math.fabs(x1 - z)

    if k > 100:
        break

    if de <= e:
        break

    y0 = y1
    y1 = f(z)
    x0 = x1
    x1 = z

print(z)
print('%.4f' % f(z))
