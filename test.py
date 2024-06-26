#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%

# load data
paths = [r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-I.csv', r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-V.csv']

data_current = pd.read_csv(paths[0], skiprows=5, index_col=False, header=None)
data_voltage = pd.read_csv(paths[1], skiprows=5, index_col=False, header=None)

print(data_current.head())
print(data_voltage.head())

print(data_current.shape)

current_array = np.array([data_current.iloc[i] for i in range(data_current.shape[0])])
voltage_array = np.array([data_voltage.iloc[i] for i in range(data_current.shape[0])])

# %%

plt.plot(current_array.ravel())
plt.title('Current Injection')
plt.show()

plt.plot(voltage_array.ravel()[300_000:350000])
plt.title('Voltage Recorded')
plt.show()
