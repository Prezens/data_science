# scipy_optimize

from scipy.optimize import fsolve
import math


def equations(p):
    x, y = p
    return math.tan(x * y + 0.1) - x ** 2, 0.6 * x ** 2 + 2 * y ** 2 - 1


x, y = fsolve(equations, (1, 1))
print('Корни СУ: ', x, ',', y)
# print(equations((x, y)))
