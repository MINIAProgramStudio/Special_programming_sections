import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

#Частина 1ша

#pandas dataframe
dataframe = pd.read_csv("data/data_1.txt", sep = ";", low_memory = False)
dataframe = dataframe.dropna()
dataframe["Global_active_power"] = dataframe["Global_active_power"].astype(float)
dataframe["Global_reactive_power"] = dataframe["Global_reactive_power"].astype(float)
dataframe["Voltage"] = dataframe["Voltage"].astype(float)
dataframe["Global_intensity"] = dataframe["Global_intensity"].astype(float)
dataframe["Sub_metering_1"] = dataframe["Sub_metering_1"].astype(float)
dataframe["Sub_metering_2"] = dataframe["Sub_metering_2"].astype(float)
dataframe["Sub_metering_3"] = dataframe["Sub_metering_3"].astype(float)

#task 1
start = time.time_ns()
pd_selection_task_1 = dataframe.loc[dataframe["Global_active_power"] > 5]
end = time.time_ns()
pd_1_time = (end - start)/(10**6)
print("Pandas completed task 1 in " + str(pd_1_time) + " ms")

#task 2
start = time.time_ns()
pd_selection_task_2= dataframe.loc[dataframe["Global_active_power"] > 235]
end = time.time_ns()
pd_2_time = (end - start)/(10**6)
print("Pandas completed task 2 in " + str(pd_2_time) + " ms")

#task 3
start = time.time_ns()
amp_cap = dataframe.loc[dataframe["Global_intensity"] <= 20]
amp_cap = amp_cap.loc[amp_cap["Global_intensity"] >= 19]
pd_selection_task_3 = amp_cap.loc[amp_cap["Sub_metering_2"]>amp_cap["Sub_metering_3"]]
end = time.time_ns()
pd_3_time = (end - start)/(10**6)
print("Pandas completed task 3 in " + str(pd_3_time) + " ms")

#task 4
start = time.time_ns()
selection = dataframe.sample(5*10**5)
avg_1 = selection["Sub_metering_1"].mean()
avg_2 = selection["Sub_metering_2"].mean()
avg_3 = selection["Sub_metering_3"].mean()
end = time.time_ns()
pd_4_time = (end - start)/(10**6)
print("Pandas completed task 4 in " + str(pd_4_time) + " ms")

#task 5
start = time.time_ns()
time_cap = dataframe[dataframe["Time"]>="18:00:00"]
power_cap = time_cap[time_cap['Global_active_power']+time_cap['Global_reactive_power']>6]
selection = power_cap[power_cap["Sub_metering_2"] > power_cap['Sub_metering_1']]
selection = power_cap[power_cap["Sub_metering_2"] > power_cap['Sub_metering_3']]
half_top = selection.head(int(selection.shape[0]/2))
half_bottom = selection.tail(int(selection.shape[0]/2+0.5))
half_top_every_3rd = half_top.iloc[::3,:]
half_bottom_every_4th = half_bottom.iloc[::4,:]
end = time.time_ns()
pd_5_time = (end - start)/(10**6)
print("Pandas completed task 5 in " + str(pd_5_time) + " ms")

#numpy
array = dataframe.to_numpy()

#task 1
start = time.time_ns()
mask = (array[:,2] > 5)
np_selection_task_1 = array[mask,:]
end = time.time_ns()
np_1_time = (end - start)/(10**6)
print("Numpy completed task 1 in " + str(np_1_time) + " ms")

#task 2
start = time.time_ns()
mask = (array[:,4] > 235)
np_selection_task_2 = array[mask,:]
end = time.time_ns()
np_2_time = (end - start)/(10**6)
print("Numpy completed task 2 in " + str(np_2_time) + " ms")

#task 3
start = time.time_ns()
mask = (array[:,5] <= 20)
temp_array = array[mask]
mask = (temp_array[:,5] >= 19)
temp_array = temp_array[mask]
mask = (temp_array[:, 7] > temp_array[:, 8])
np_selection_task_3 = temp_array[mask]
end = time.time_ns()
np_3_time = (end - start)/(10**6)
print("Numpy completed task 3 in " + str(np_3_time) + " ms")

#task 4
start = time.time_ns()
temp_array = array
np.random.shuffle(temp_array)
temp_array = temp_array[0:500000]
np_avg_1 = np.mean(temp_array[:,6])
np_avg_2 = np.mean(temp_array[:,7])
np_avg_3 = np.mean(temp_array[:,8])
end = time.time_ns()
np_4_time = (end - start)/(10**6)
print("Numpy completed task 4 in " + str(np_4_time) + " ms")

#task 5
start = time.time_ns()
mask = (array[:,1] >= "18:00:00")
temp_array = array[mask]
mask = (temp_array[:,2]+temp_array[:,3] >= 6)
temp_array = temp_array[mask]
mask = (temp_array[:,7] > temp_array[:,6])
temp_array = temp_array[mask]
mask = (temp_array[:,7] > temp_array[:,8])
array_head = temp_array[0:int(len(temp_array)/2)]
array_head = array_head[0::3]
array_tail = temp_array[int(len(temp_array)/2+0.5):]
array_tail = array_tail[0::4]
end = time.time_ns()
np_5_time = (end - start)/(10**6)
print("Numpy completed task 5 in " + str(np_5_time) + " ms")


#Висновок:
'''
Оскільки реалізація завдань методами Pandas виконується у 2-30 разів швидше ніж Numpy, і Pandas пропонує більш зручні
методи відбору, то в усіх ситуаціях доречно і ефективно використовувати методи Pandas 
'''

#Частина 2га
#Dataframe
dataframe = pd.read_csv("data/bank-full.csv", sep=";")
dataframe = dataframe.dropna()

def standartize(dataframe, cloumn_index):
    min_val = dataframe[cloumn_index].min()
    max_val = dataframe[cloumn_index].max()
    dataframe[cloumn_index] = (dataframe[cloumn_index]-min_val)/(max_val-min_val)
    return dataframe
dataframe=standartize(dataframe, 'balance')
dataframe=standartize(dataframe, 'age')
dataframe=standartize(dataframe, 'duration')
dataframe['range'] = pd.cut(dataframe.balance, bins=[0, 0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
tab = pd.crosstab(dataframe.range, dataframe.range).add_suffix('_Count')
dataframe.range.value_counts().plot.bar()
plt.show()

dataframe['range'] = pd.cut(dataframe.balance, bins=[0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
dataframe.range.value_counts().plot.bar()
plt.show()


plot = dataframe.sort_values('age').plot(y='balance', x='age')
plt.show()