import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import PyTaCo

#Завдання 1
#Генерація випадкових даних
k = 2
b = 1
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
        if deviation>0.999 and deviation<1.001:
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
    plot = [0]*n_iter
    for i in range(n_iter):
        y_i = b_regr + x*k_regr
        deviation = (y_i/(y+0.0000001)).mean()
        plot[i] = deviation
        if deviation>0.99999 and deviation<1.00001:
            break
        dldb = y.sum() - y_i.sum()
        dldk = 0
        for ii in range(len(x)):
            dldk += x[ii]*(y[ii] - y_i[ii])
        dldb *=(-2)/len(x)
        dldk *= (-2) / len(x)
        b_regr = b_regr - learning_rate * dldb
        k_regr = k_regr - learning_rate * dldk
    return plot

'''
#визначення оптимальних параметрів
def closest_position(list_in, target):
    if target == 0:
        raise Exception("Error in closest_position(list_in, target): Target must not be 0")
    closest_deviation = 0
    closest_deviation_pos = 0
    for i in range(len(list_in)):
        value = list_in[i]
        deviation = value/target
        if abs(1-deviation) < abs(1-closest_deviation):
            closest_deviation = deviation
            closest_deviation_pos = i
    return [closest_deviation, closest_deviation_pos]



learning_rate_best = 0
iterations_best = 0
progress_bar = tqdm(total = 2750)
plot_array_closest = []
for learning_rate in range(-10,1):
    if learning_rate <= 0:
        learning_rate = 2**(learning_rate)
    plot_array = []
    for kk in range(1,6):
        for bb in range(1,6):
            for noise_num in range(10):
                yy = x*bb+kk + np.random.randn(num_points)
                plot_array.append([closest_position(regression_plot(x,yy,5**iterations,learning_rate),1) for iterations in range(3,6)])
                progress_bar.update(1)
    plot_array_closest.append(plot_array)

pos = [0,0]
plot_array_raw_results = [["Learning_rate"],["Кількість ітерацій"],["Середня точність"]]
for learning_rate in range(11):
    accuracy = 0
    length = len(plot_array_closest[learning_rate])
    for iterations in range(5,6):
        ac_length = 0
        for value in plot_array_closest[learning_rate][iterations]:
            if value[0] < 1:
                accuracy += value[0]
            else:
                accuracy += 1/value[0]
            ac_length+=1
        plot_array_raw_results[0].append(2**(learning_rate-5))
        plot_array_raw_results[2].append(100*accuracy/ac_length)
        plot_array_raw_results[1].append(5**iterations)
results = PyTaCo.PyTableConsole(plot_array_raw_results)
results.sort_by_column(2,1)
print(results)
'''
#отримані оптимальні вхідні параметри: 0.03125 625
#ці параметри можуть відрізнятись через випадковість шуму під час перевірок
#графік з регресією
plt.scatter(x, y, label='Дані з шумом')
plt.plot(x, k * x + b, color='red', label='Задана пряма')
plt.plot(x, k_predicted * x + b_predicted, color='blue', label='Знайдена пряма')
regr = regression(x,y,625,0.00625)
plt.plot(x, regr[0]*x+regr[1], color='green', label='Знайдена пряма, регресія')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



#графік точності від кількості ітерацій
plt.plot(regression_plot(x,y,1000,0.00625), color='red')
plt.xlabel('ітерація')
plt.ylabel('точність')
plt.legend()
plt.show()