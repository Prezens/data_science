# Working with matrices


import numpy as np
import sympy as sp

print('ИССЛЕДОВАНИЕ СИСТЕМЫ УРАВНЕНИЙ НА СОВМЕСТИМОСТЬ')
print('Матрица коэффициентов системы')

A = np.array([[7, -12, 4, 2],
              [3, 21, 8, 5],
              [1, 7, -14, 18],
              [21, 4, 32, 11]
])
print(A, '\n')

print('Вектор свободных членов')
b = np.array([[-8.8],
              [23.7],
              [-3],
              [30.1]
])
print(b, '\n')

print('Определитель системы')
DA = np.linalg.det(A)
print(DA, '\n')

print('Число уравнений системы')
m = len(A)
print(m, '\n')

print('Формирование расширенной матрицы: D = [A B]')
D = np.append(A, b, axis=1)
print(D, '\n')

print('Ранг расширенной матрицы D')
RD = np.linalg.matrix_rank(D)
print(RD, '\n')

print('Ранг матрицы коэффициентов А')
RA = np.linalg.matrix_rank(A)
print(RA, '\n')

if RD > RA:
    print('Вывод: система уравнений несовместна')
elif (RD == RA) and (RA == m):
    print('Вывод: система имеет единственное решение')
else:
    print('Вывод: система имеет бесконечное число решений')

print()

print('РЕШЕНИЕ СИСТЕМЫ УРАВНЕНИЙ МЕТОДОМ ОБРАТНОЙ МАТРИЦЫ')
print('Решение: X = inv(A)*B')

X = np.dot(np.linalg.inv(A), b)
print(X)

# s = np.linalg.solve(A, b)

print('Проверка: A * X = B')
print(np.dot(A, X))


print('\n\n')
print('РЕШЕНИЕ СИСТЕМЫ УРАВНЕНИЙ МЕТОДОМ КРАМЕРА')

print('Первая вспомогательная матрица')
A1 = A.copy()
A1[:,0] = b[:,0]
print(A1, '\n')

print('Вторая вспомогательная матрица')
A2 = A.copy()
A2[:,1] = b[:,0]
print(A2, '\n')

print('Третья вспомогательная матрица')
A3 = A.copy()
A3[:,2] = b[:,0]
print(A3, '\n')

print('Четвертая вспомогательная матрица')
A4 = A.copy()
A4[:,3] = b[:,0]
print(A4, '\n')

print('Главный определитель')
D = np.linalg.det(A)
print('%.2f' % D)

d = []
print('\n', 'Определители вспомогательных матриц')
d.append(np.linalg.det(A1))
print('d1 = %.1f' % d[0])
d.append(np.linalg.det(A2))
print('d2 = %.1f' % d[1])
d.append(np.linalg.det(A3))
print('d3 = %.1f' % d[2])
d.append(np.linalg.det(A4))
print('d4 = %.1f' % d[3])

print('\n', 'Вектор неизвестных')
X = d / D
print(X, '\n')

print('Проверка: B = ')
print(np.dot(A, X))


print('\n\n')
print('РЕШЕНИЕ СИСТЕМЫ УРАВНЕНИЙ МЕТОДОМ ГАУССА', '\n')

print('Формирование расширенной матрицы: D = [A B]')
D = np.append(A, b, axis=1)
print(D, '\n')

print('Приведение матрицы D к треугольному виду C = rref(D)')
C = sp.Matrix(D)
C = C.rref()[0]
print(C)

print('\n', 'Выделение последнего столбца матрицы С (решение системы)')
X = C.col(-1)
print(X)

print('Проверка: A*X-B')
X = np.array(X)

print(np.dot(A, X) - b)
