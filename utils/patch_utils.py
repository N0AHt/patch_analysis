"""
Utilities for patch clamp loading and analysis from labview/axon setup
"""

import pandas as pd
import os
from datetime import datetime
import numpy as np
from collections import defaultdict


def extract_data_and_metadata(csv_file_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Take a csv file generated by labview and parse it into data, and metadata.
    returns a tuple of two dataframes, one containing metadata for the recording the other with the recording

    :param csv_file_path: path to the voltage or current .csv recording file
    :return: tuple of pandas data frames
    """

    data = pd.read_csv(csv_file_path, skiprows=5, header=None)

    metadata = pd.read_csv(csv_file_path, sep=':', header=None, nrows=3, index_col=False)
    metadata.index = ['resolution', 'num_points', 'date']
    metadata.columns = ['original_title', 'value']
    metadata = metadata.T

    return data, metadata


# there is a better way to represent this as a dataframe... One df with metadata, data, voltage, and current
# all collected and grouped by stimulation


def make_patch_dataframe(path_to_voltage_csv: str, path_to_current_csv: str, path_to_stimulation_csv: str = None) -> pd.DataFrame:
    
    dataV_array, metaV_array = extract_data_and_metadata(path_to_voltage_csv)
    dataI_array, _ = extract_data_and_metadata(path_to_current_csv)
    # it is assumed that the metadata for the voltage and current recordings are the same

    if path_to_stimulation_csv:
        data_aux, _ = extract_data_and_metadata(path_to_stimulation_csv)
        data_aux.loc[data_aux.index[-1] + 1] = [0] * len(data_aux.columns)
    else:
        data_aux = None

    # extract better metadata from the files

    # extract some metadata about the file used: date and number of the cell/recording
    date_original = metaV_array.date.value.strip()
    date_obj = datetime.strptime(date_original, "%m/%d/%Y")
    date = date_obj.strftime("%Y/%m/%d")

    recording_name = os.path.basename(path_to_voltage_csv).split(".")[0].split('-')[0]


    row_names = ['date', 'paths', 'metadata', 'voltage', 'current', 'stimulation']
    dataframe = pd.DataFrame({recording_name: [date, [path_to_voltage_csv, path_to_current_csv], metaV_array,
                                               dataV_array, dataI_array, data_aux]}, index=row_names, dtype='object')

    return dataframe


def make_dataset_dataframe(path_to_folder: str, stim: bool = False) -> pd.DataFrame:
    """
    Make a dataframe containing multiple recordings from a single cell. Takes a folder of recordings and turns it into
    a dataframe with columns=recording, rows=attributes/data from that recording.


    :param path_to_folder: path to a folder of data
    :return: a pandas dataframe for all recordings from one cell/from one folder
    """

    files = os.listdir(path_to_folder)  # return a list of files in the folder
    files = [os.path.abspath(os.path.join(path_to_folder, file)) for file in files]


    # cool hashmap method for organising the files! leetcode ;)
    filedict = dict()
    for file in files:
        file_title = (os.path.basename(file).split(".")[0].split('-')[0])
        if file_title in filedict:
            filedict[file_title].append(file)
        else:
            filedict[file_title] = [file]

    if stim:
    # TODO: make sure that current and voltage files are in the correct order! this is really un robust atm. Uses location in the dictionary!
        df_list = [ make_patch_dataframe(path_to_voltage_csv = filedict[key][2], path_to_current_csv = filedict[key][0], 
                                        path_to_stimulation_csv = filedict[key][1]) for key in filedict.keys() ]
        dataset = pd.concat(df_list, axis=1)

        return dataset
    else:
        df_list = [ make_patch_dataframe(path_to_voltage_csv = filedict[key][1], path_to_current_csv = filedict[key][0]) for key in filedict.keys() ]
        dataset = pd.concat(df_list, axis=1)

        return dataset
