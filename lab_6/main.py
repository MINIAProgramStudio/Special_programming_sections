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