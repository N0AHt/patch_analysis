import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import patch_utils as patch
import seaborn as sms

datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-V.csv'
datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-I.csv'
#
# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-I.csv'


data_V, metadata_V = patch.extract_data_and_metadata(datafile_voltage)
data_I, metadata_I = patch.extract_data_and_metadata(datafile_current)

# %%

num_points = int(metadata_V.num_points.value)
resolution = int(metadata_V.resolution.value)
x_axis = np.linspace(0, (num_points / resolution), num_points)

# multi plot
multiplot = plt.figure(figsize=(10, 6))
for i in range(len(data_V)):
    plot_data = data_V.iloc[i].tolist()
    plt.plot(x_axis, plot_data, linestyle='-')

# Add titles and labels
# for these cells, day 0 was August 12th
plt.title('Current Clamp Recording - DIV 16')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')

# Show grid
plt.grid(True)

# Display the plot
plt.show()

# %%

# plot with current

# Concatenate all lists into one long list
data_long_V = data_V.values.flatten()
data_long_I = data_I.values.flatten()
x_axis_long = np.linspace(0, len(data_long_V) / resolution, len(data_long_V))

fig_long, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# First subplot
ax1.plot(x_axis_long, data_long_V, color='b', linestyle='-')
ax1.set_title('Induced APs at 16 DIV')
ax1.set_ylabel('Voltage (mV)')
ax1.grid(True)

# Second subplot
ax2.plot(x_axis_long, data_long_I, color='r', linestyle='--')
ax2.set_title('Applied Current')
ax2.set_xlabel('time (ms)')
ax2.set_ylabel('Current (pA)')
ax2.grid(True)

plt.show()
