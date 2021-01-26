# importing packages for lab
import os
import numpy as np
import pandas as pd
import pyeeg
import matplotlib.pyplot as plt
from scipy.io import loadmat

# path to acquisition file
os.chdir('/Users/umreenimam/documents/masters/masters_classes/cs_5310/week_2/lab_1')
# setting filename variable
filename = 'Acquisition-15-data.mat'
# loading data into environment via loadmat func from scipy.io
data = loadmat(filename)
# setting eeg variable to the contents of 'data' variable
eeg = data['data']

# creating eeg_data DataFrame using pandas DataFrame function
eeg_data = pd.DataFrame(eeg)
# transposing dataframe to have 63296 rows & 34 columns
# using .T function from pandas package
eeg_data_t = eeg_data.T
# extract columns from dataframe
#print(eeg_data_t.loc[:, 0])

# EEG values mean
# using axis=1 to run function across 34 channels
data_means = np.mean(eeg_data_t, axis=1)

# EEG values standard deviation
# using axis=1 to run function across 34 channels
data_sd = np.std(eeg_data_t, axis=1)

# calculating plot info
x = data_means - data_sd
y = data_means + data_sd

# creating scatterplot
colors = ("red", "blue", "green")
fig = plt.figure(figsize=(6, 6))
plt.scatter(x, y, linewidths=1, alpha=1, s=200, c=data_means, label=colors, edgecolors='black')
plt.show()

# creating empty array for later use
bin_powers = []

# bin_power() function
bin_power_0 = pyeeg.bin_power(X=eeg_data_t.loc[:, 0], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_1 = pyeeg.bin_power(X=eeg_data_t.loc[:, 1], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_2 = pyeeg.bin_power(X=eeg_data_t.loc[:, 2], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_3 = pyeeg.bin_power(X=eeg_data_t.loc[:, 3], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_4 = pyeeg.bin_power(X=eeg_data_t.loc[:, 4], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_5 = pyeeg.bin_power(X=eeg_data_t.loc[:, 5], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_6 = pyeeg.bin_power(X=eeg_data_t.loc[:, 6], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_7 = pyeeg.bin_power(X=eeg_data_t.loc[:, 7], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_8 = pyeeg.bin_power(X=eeg_data_t.loc[:, 8], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_9 = pyeeg.bin_power(X=eeg_data_t.loc[:, 9], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_10 = pyeeg.bin_power(X=eeg_data_t.loc[:, 10], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_11 = pyeeg.bin_power(X=eeg_data_t.loc[:, 11], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_12 = pyeeg.bin_power(X=eeg_data_t.loc[:, 12], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_13 = pyeeg.bin_power(X=eeg_data_t.loc[:, 13], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_14 = pyeeg.bin_power(X=eeg_data_t.loc[:, 14], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_15 = pyeeg.bin_power(X=eeg_data_t.loc[:, 15], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_16 = pyeeg.bin_power(X=eeg_data_t.loc[:, 16], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_17 = pyeeg.bin_power(X=eeg_data_t.loc[:, 17], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_18 = pyeeg.bin_power(X=eeg_data_t.loc[:, 18], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_19 = pyeeg.bin_power(X=eeg_data_t.loc[:, 19], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_20 = pyeeg.bin_power(X=eeg_data_t.loc[:, 20], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_21 = pyeeg.bin_power(X=eeg_data_t.loc[:, 21], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_22 = pyeeg.bin_power(X=eeg_data_t.loc[:, 22], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_23 = pyeeg.bin_power(X=eeg_data_t.loc[:, 23], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_24 = pyeeg.bin_power(X=eeg_data_t.loc[:, 24], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_25 = pyeeg.bin_power(X=eeg_data_t.loc[:, 25], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_26 = pyeeg.bin_power(X=eeg_data_t.loc[:, 26], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_27 = pyeeg.bin_power(X=eeg_data_t.loc[:, 27], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_28 = pyeeg.bin_power(X=eeg_data_t.loc[:, 28], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_29 = pyeeg.bin_power(X=eeg_data_t.loc[:, 29], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_30 = pyeeg.bin_power(X=eeg_data_t.loc[:, 30], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_31 = pyeeg.bin_power(X=eeg_data_t.loc[:, 31], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_32 = pyeeg.bin_power(X=eeg_data_t.loc[:, 32], Band=[0.5, 4, 7, 12, 30], Fs=1024)
bin_power_33 = pyeeg.bin_power(X=eeg_data_t.loc[:, 33], Band=[0.5, 4, 7, 12, 30], Fs=1024)








