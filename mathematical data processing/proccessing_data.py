# Statistical processing of experimental data. Descriptive characteristics of a one-dimensional random sample


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats.distributions import chi2
from math import sqrt


def main(x6):
    print(x6[0], '\n\n')

    for i in range(len(x6[0])):
        print('Значение %d элемента:' % (i + 1), x6[0][i])

    n = len(x6[0])
    print('Длина:', n)

    sum_nparray = x6.sum()
    print('Сумма:', sum_nparray)

    min_nparray = x6.min()
    print('Минимальный элемент:', min_nparray)

    max_nparray = x6.max()
    print('Максимальный элемент:', max_nparray)

    swing_nparray = max_nparray - min_nparray
    print('Размах:', swing_nparray)

    v = n - 1
    print('Число степеней свободы:', v)

    Mx = np.mean(x6)
    print('Среднее арифметическое:', Mx)

    Me = np.median(x6)
    print('Медиана:', Me)

    Dx = x6.var(ddof=1)
    print('Дисперсия:', Dx)

    Sx = x6.std(ddof=1)
    print('Среднеквадратическое отклонение:', Sx)

    Vx = (Sx / Mx) * 100
    print('Коэффициент вариации:', Vx)

    Ax = st.skew(x6[0])
    print('Коэффициент асимметрии:', Ax)

    Ex = st.kurtosis(x6[0])
    print('Коэффициент эксцесса:', Ex)

    p = 0.95
    t = st.t.ppf(1 - p / 2, v)
    Mxd = (Mx - (Sx * t) / sqrt(n), (Mx + (Sx * t) / sqrt(n)))
    print('Доверительный интервал математического ожидания: {:.4f} <= Mx <= {:.4f}'.format(Mxd[0], Mxd[1]))

    chi2l = chi2.ppf(1 - p / 2, df=v)
    chi2r = chi2.ppf(p / 2, df=v)
    Dxd = (v * Dx / chi2l, v * Dx / chi2r)
    print('Доверительный интервал генеральной дисперсии: {:.4f} <= Dx <= {:.4f}'.format(Dxd[0], Dxd[1]))

    Da = 6 * (n - 1) / (n + 1) / (n + 3)
    De = 24 * n * (n - 2) * (n - 3) / (n + 1) ** 2 / (n + 3) / (n + 5)
    Axd = (Ax - sqrt(Da / p), Ax + sqrt(Da / p))
    print('Доверительный интервал генеральной асимметрии: {:.4f} <= Ax <= {:.4f}'.format(Axd[0], Axd[1]))

    Exd = (Ex - sqrt(De / p), Ex + sqrt(De / p))
    print('Доверительный интервал генерального эксцесса: {:.4f} <= Ex <= {:.4f}'.format(Exd[0], Exd[1]))

    Q1 = np.percentile(x6, 25)
    Q2 = np.percentile(x6, 50)
    Q3 = np.percentile(x6, 75)

    data = [x6[0]]

    _, bp = plt.subplots()
    bp.set_title('Блочная диаграмма')
    plt.ylabel('Значения элементов выборки')
    bp.plot(1, Mx, marker='o', markersize=8)
    bp.text(1.1, Q1, 'Q1-25%', fontsize=12, color='blue')
    bp.text(1.1, Q2, 'Q2-50% медиана', fontsize=12, color='orange')
    bp.text(1.1, Q3, 'Q3-75%', fontsize=12, color='blue')
    bp.text(0.80, Mx, 'среднее', fontsize=12, color='black')
    bp.boxplot(data, sym='b+', notch=True)
    plt.show()


if __name__ == '__main__':
    mat = scipy.io.loadmat('data_test.mat')
    x6 = mat.get('X6')

    main(x6)

#https://physics.susu.ru/vorontsov/language/numpy.html
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array
#https://tproger.ru/translations/basic-statistics-in-python-descriptive-statistics/
#https://physics.susu.ru/vorontsov/language/numpy.html
