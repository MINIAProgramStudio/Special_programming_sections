import numpy as np
import matplotlib.pyplot as plt

#Завдання 1
#Генерація випадкових даних
k = 2
b = 5
num_points = 1000
noise = np.random.randn(num_points)
x = np.linspace(0, 10, num_points)
y = k * x + b + noise

plt.scatter(x, y, label='Дані з шумом')
plt.plot(x, k * x + b, color='red', label='Задана пряма')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#пошук b_predicted і k_predicted
x_mean = x.mean()
y_mean = y.mean()
sum_1 = 0
sum_2 = 0
for i in range(len(x)):
    sum_1+=(x[i]-x_mean)*(y[i]-y_mean)
    sum_2+=(x[i]-x_mean)**2
k_predicted = sum_1/sum_2
b_predicted = y_mean-k_predicted*x_mean
print(k_predicted)
print(b_predicted)
#порівняння з polyfit
poly = np.polyfit(x,y,1)
print(poly)
#загальний графік
plt.scatter(x, y, label='Дані з шумом')
plt.plot(x, k * x + b, color='red', label='Задана пряма')
plt.plot(x, k_predicted * x + b_predicted, color='blue', label='Знайдена пряма')
plt.plot(x, poly[0] * x + poly[1], color='green', label='Знайдена пряма, numpy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#завдання 2
def regression(x,y,n_iter = 1000, learning_rate = 0.01,b_0 = 0,k_0=1):
    b_regr = b_0
    k_regr = k_0
    for i in range(n_iter):
        y_i = b_regr + x*k_regr
        deviation = (y_i/y).mean()
        if deviation>0.99 and deviation<1.01:
            break
        dldb = 0
        dldk = 0
        for i in range(len(x)):
            dldb += y[i]-y_i[i]
            dldk += x[i]*(y[i] - y_i[i])
        dldb *=(-2)/len(x)
        dldk *= (-2) / len(x)
        b_regr= b_regr - learning_rate * dldb
        k_regr= k_regr - learning_rate * dldk
    return [k_regr,b_regr]
print(regression(x,y))

def regression_plot(x,y,n_iter = 1000, learning_rate = 0.01,b_0 = 0,k_0=1):
    b_regr = b_0
    k_regr = k_0
    plot = []
    for i in range(n_iter):
        y_i = b_regr + x*k_regr
        deviation = (y_i/(y+0.00000000001)).mean()
        plot.append(deviation)
        if deviation>0.99 and deviation<1.01:
            break
        dldb = 0
        dldk = 0
        for i in range(len(x)):
            dldb += y[i]-y_i[i]
            dldk += x[i]*(y[i] - y_i[i])
        dldb *=(-2)/len(x)
        dldk *= (-2) / len(x)
        b_regr= b_regr - learning_rate * dldb
        k_regr= k_regr - learning_rate * dldk
    return plot


#визначення оптимальних параметрів
learning_rate_best = 0
iterations_best = 0
for learning_rate in range(-10,10):
    if learning_rate <= 0:
        learning_rate = 10**(learning_rate)
    plot_array = []
    for k in range(-10,10):
        for b in range (-10,10):
            plot_array.append(regression_plot(x,x*b+k,5000))
    plot_array_closest = plot_array[:].




#графік точності від кількості ітерацій


plt.plot(regression_plot(x,y), color='red')
plt.xlabel('ітерація')
plt.ylabel('точність')
plt.legend()
plt.show()

#