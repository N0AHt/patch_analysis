import patch_utils as patch
import plot_utils as p_plot


# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-I.csv'

datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-V.csv'
datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec1_cell1-I.csv'

folder_path = r'C:\Users\jl5675\Desktop\Noah\data\patch2'
df = patch.make_dataset_dataframe(folder_path)

# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\github\patch_analysis\data\data_cell1-I.csv'

# datafile_voltage = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec4_holding_cell1-V.csv'
# datafile_current = r'C:\Users\jl5675\Desktop\Noah\data\patch2\rec4_holding_cell1-I.csv'


# data_V, metadata_V = patch.extract_data_and_metadata(datafile_voltage)
# data_I, metadata_I = patch.extract_data_and_metadata(datafile_current)

patchdata = patch.make_patch_dataframe(datafile_voltage, datafile_current)
rec1 = patchdata.rec1_cell1

# df = dataframe.loc['paths', 'rec1_cell1'] # need to access row and column! if I only use loc['row_name'] it will return a series!
# note that you can force the return of a dataframe by using double brackets loc[ [row_name] ] (Returns a DataFrame (because pandas treats this as accessing multiple rows, even if it's only one).)

file_name = patchdata.columns[0]
date = patchdata.loc['date', 'rec1_cell1']
title = 'DIV 16; ' + file_name + '; ' + date

# %%

p_plot.multiplot(rec1['voltage'], rec1['metadata'], title)

# %%

p_plot.time_plot(rec1['voltage'], rec1['current'], rec1['metadata'], title)

# %%

# plt.plot(data_V.iloc[31])
# plt.show()
