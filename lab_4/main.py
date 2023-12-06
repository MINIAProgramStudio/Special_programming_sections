import numpy as np
import pandas as pd

#dataframe
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
pd_selection_task_1 = dataframe.loc[dataframe["Global_active_power"] > 5]

#task 2
pd_selection_task_2= dataframe.loc[dataframe["Global_active_power"] > 235]

#task 3
amp_cap = dataframe.loc[dataframe["Global_intensity"] <= 20]
amp_cap = amp_cap.loc[amp_cap["Global_intensity"] >= 19]
pd_selection_task_3 = amp_cap.loc[amp_cap["Sub_metering_2"]>amp_cap["Sub_metering_3"]]

#task 4
selection = dataframe.sample(5*10**5)
avg_1 = selection["Sub_metering_1"].mean()
avg_2 = selection["Sub_metering_2"].mean()
avg_3 = selection["Sub_metering_3"].mean()

#task 5
time_cap = dataframe[dataframe["Time"]>="18:00:00"]
selection = time_cap[time_cap["Sub_metering_2"]>=(time_cap['Global_active_power']+time_cap['Global_reactive_power'])/2]
half_top = time_cap.head(int(time_cap.shape[0]/2))
half_bottom = time_cap.tail(int(time_cap.shape[0]/2+0.5))
half_top_every_3rd = half_top.iloc[::3,:]
half_bottom_every_4th = half_bottom.iloc[::4,:]