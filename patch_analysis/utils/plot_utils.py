# plotting utilities for patch clamp recordings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def multiplot(data: pd.DataFrame, metadata: pd.DataFrame, title: str, show: bool = True) -> None:
    '''
    This function plots patch data recorded via jesus' labview program that has been processed by the
    extract_data_and_metadata() function in patch utils

    Plots each trial in one plot on top of one another

    :param data: Voltage dataframe of recorded data
    :param metadata: dataframe of metadata from the recording
    :return: void, no value is returned
    '''

    num_points = int(metadata.num_points.value)
    resolution = int(metadata.resolution.value)
    x_axis = np.linspace(0, (num_points / resolution), num_points)

    # multi plot
    plt.figure(figsize=(10, 6))
    for i in range(len(data)):
        plot_data = data.iloc[i].tolist()
        plt.plot(x_axis, plot_data, linestyle='-')

    # Add titles and labels
    plt.title(title)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (mV)')

    # Show grid
    plt.grid(True)

    # Display the plot
    if show:
        plt.show()


def time_plot(data_voltage: pd.DataFrame, data_current: pd.DataFrame, metadata: pd.DataFrame, title: str = None, show: bool = True) -> None:
    '''
    plot all data and voltage recordings over time in a recording

    :param data_voltage:
    :param data_current:
    :param metadata:
    :return:
    '''

    # plot with current

    # Concatenate all lists into one long list
    data_long_V = data_voltage.values.flatten()
    data_long_I = data_current.values.flatten()
    resolution = int(metadata.resolution.value)
    x_axis_long = np.linspace(0, len(data_long_V) / resolution, len(data_long_V))

    fig_long, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # First subplot
    ax1.plot(x_axis_long, data_long_V, color='b', linestyle='-')
    ax1.set_title('Recorded Voltage')
    ax1.set_ylabel('Voltage (mV)')
    ax1.grid(True)

    # Second subplot
    ax2.plot(x_axis_long, data_long_I, color='r', linestyle='--')
    ax2.set_title('Injected Current')
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Current (pA)')
    ax2.grid(True)

    fig_long.suptitle(title)

    if show:
        plt.show()


def stim_plot(data_voltage, data_stim, metadata, title):

    num_points = int(metadata.num_points.value)
    resolution = int(metadata.resolution.value)
    x_axis = np.linspace(0, (num_points / resolution), num_points)

    crosses = find_threshold_crosses(data_stim)

    # multi plot
    plt.figure(figsize=(10, 6))
    for i in range(len(data_voltage)):
        plot_data = data_voltage.iloc[i].tolist()
        plt.plot(x_axis, plot_data, linestyle='-')

    # add colour when stimulation is applied
    for cross in crosses:
        print(cross)
        plt.axvspan(data_voltage.index[cross[0]], data_voltage.index[cross[1]], color='r', alpha=0.4, lw=0)

    # Add titles and labels
    plt.title(title)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (mV)')

    # Show grid
    plt.grid(True)

    plt.show()


def time_plot_stim(data_voltage: pd.DataFrame, data_stimulation: pd.DataFrame, metadata: pd.DataFrame, title: str = None, show: bool = True) -> None:

    '''
    plot all voltage recordings over time in a recording with overlay of stimulation application

    :param data_voltage:
    :param data_stimulation:
    :param metadata:
    :return:
    '''

    volts = data_voltage.values.flatten()
    stims = data_stimulation

    resolution = int(metadata.resolution.value)
    x_axis = np.linspace(0, len(volts) / resolution, len(volts))

    crosses = find_threshold_crosses(stims)

    plt.figure(figsize=(10, 6))

    plt.plot(x_axis, volts)
    for cross in crosses:
        plt.axvspan(cross[0]/resolution, cross[1]/resolution, color = 'r', alpha=0.2, lw=0, label = 'Stimulation Applied')

    plt.title(title)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (mV)')

    plt.legend

    plt.grid(True)

    plt.show()


# utility for stim plots. May be useful for other things too. If so will move into patch_utils
def find_threshold_crosses(data_stim):
    #find on/off stim points
    stim = data_stim.values.flatten()
    threshold = stim.max()/2

    indices_positive = np.where((stim[:-1] < threshold) & (stim[1:] >= threshold))[0] + 1 # From chatGPT 
    indices_negative = np.where((stim[:-1] > threshold) & (stim[1:] <= threshold))[0] + 1

    '''
    array[:-1]: This slices the array from the start up to, but not including, the last element. Essentially, it excludes the last element. For example, if array = [1, 3, 2, 5], then array[:-1] results in [1, 3, 2].

    array[1:]: This slices the array starting from the second element to the end. For example, if array = [1, 3, 2, 5], then array[1:] results in [3, 2, 5].

    By comparing these slices:

    array[:-1] < threshold: Checks if each element in array up to the second-to-last is less than the threshold.
    array[1:] >= threshold: Checks if each element in array starting from the second element is greater than or equal to the threshold.
    The boolean expression (array[:-1] < threshold) & (array[1:] >= threshold) evaluates to True where the value crosses the threshold from below to above.
    '''

    # combined_indices = np.concatenate((indices_positive, indices_negative))
    # # Sort the combined indices
    # combined_indices_sorted = np.sort(combined_indices)

    combined_indices = zip(indices_positive, indices_negative)

    return list(combined_indices)
