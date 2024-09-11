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