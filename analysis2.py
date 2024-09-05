import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import patch_utils as patch
import plot_utils as p_plot
import seaborn as sms
from datetime import datetime
import os

# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-I.csv'

datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-V.csv'
datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-I.csv'

# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-I.csv'

# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec4_holding_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec4_holding_cell1-I.csv'


data_V, metadata_V = patch.extract_data_and_metadata(datafile_voltage)
data_I, metadata_I = patch.extract_data_and_metadata(datafile_current)

#extract some metadata about the file used: date and number of the cell/recording
date_original = metadata_V.date.value.strip()
date_obj = datetime.strptime(date_original, "%m/%d/%Y")
date = date_obj.strftime("%Y/%m/%d")

file_name = os.path.basename(datafile_voltage).split(".")[0]

title = 'DIV 16 ' + file_name + ' ' + date


# %%

p_plot.multiplot(data_V, metadata_V, title)


# %%

p_plot.time_plot(data_V, data_I, metadata_V, title)


# %%

# plt.plot(data_V.iloc[31])
# plt.show()