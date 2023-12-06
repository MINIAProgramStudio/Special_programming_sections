import numpy as np
import pandas as pd
import time

#pandas dataframe
start = time.time_ns()
dataframe = pd.read_csv("data/data_1.txt", sep = ";", low_memory = False)
dataframe = dataframe.dropna()
dataframe["Global_active_power"] = dataframe["Global_active_power"].astype(float)
dataframe["Global_reactive_power"] = dataframe["Global_reactive_power"].astype(float)
dataframe["Voltage"] = dataframe["Voltage"].astype(float)
dataframe["Global_intensity"] = dataframe["Global_intensity"].astype(float)
dataframe["Sub_metering_1"] = dataframe["Sub_metering_1"].astype(float)
dataframe["Sub_metering_2"] = dataframe["Sub_metering_2"].astype(float)
dataframe["Sub_metering_3"] = dataframe["Sub_metering_3"].astype(float)
end = time.time_ns()
print("Pandas started up in " + str((end - start)/(10**6)) + " ms")

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
selection = time_cap[time_cap["Sub_metering_2"]>=(time_cap['Global_active_power']+time_cap['Global_reactive_power'])/2]
half_top = time_cap.head(int(time_cap.shape[0]/2))
half_bottom = time_cap.tail(int(time_cap.shape[0]/2+0.5))
half_top_every_3rd = half_top.iloc[::3,:]
half_bottom_every_4th = half_bottom.iloc[::4,:]
end = time.time_ns()
pd_5_time = (end - start)/(10**6)
print("Pandas completed task 5 in " + str(pd_5_time) + " ms")