import pandas as pd
import os
from datetime import datetime
import numpy as np
from collections import defaultdict
from scipy.signal import find_peaks



def find_APs(voltage_trace):

    '''
    return the index of APs found from a voltage signal input
    '''

    volts_array = voltage_trace.values.flatten()

    prom = 65
    threshold = -25
    wd = 4
    d = 50

    peaks, _ = find_peaks(volts_array, prominence = prom, threshold = threshold, width = wd, distance = d)

    return peaks


def find_current_injection(peaks, current_trace):

    '''
    find current injection needed to generate 1st AP
    '''

    current_array = current_trace.values.flatten()

    # find current at initial peak index
    if peaks.any():
        current_at_peak = current_array[peaks[0]]
        default_current = current_array[0]
        current_injection = current_at_peak - default_current
    else:
        current_injection = np.NaN

    return current_injection


def find_excitability(recording):

    voltage = recording['voltage']
    current = recording['current']

    peaks = find_APs(voltage)
    current_injection = find_current_injection(peaks, current)

    return current_injection, peaks