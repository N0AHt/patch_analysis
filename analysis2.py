import patch_utils as patch
import plot_utils as p_plot
import matplotlib.pyplot as plt


folder_path = r'C:\Users\jl5675\Desktop\Noah\data\patch2'

patchdata = patch.make_dataset_dataframe(folder_path)

# %%
#NOTE:
# df = dataframe.loc['paths', 'rec1_cell1'] # need to access row and column! if I only use loc['row_name'] it will return a series!
# note that you can force the return of a dataframe by using double brackets loc[ [row_name] ] (Returns a DataFrame (because pandas treats this as accessing multiple rows, even if it's only one).)

rec_name = patchdata.columns[0]
date = patchdata.loc['date', rec_name]
title = 'DIV 16; ' + rec_name + '; ' + date


# %%

p_plot.multiplot(patchdata.loc['voltage', rec_name], patchdata.loc['metadata', rec_name], title)

# %%

p_plot.time_plot(patchdata.loc['voltage', rec_name], patchdata.loc['current', rec_name], patchdata.loc['metadata', rec_name], title)
