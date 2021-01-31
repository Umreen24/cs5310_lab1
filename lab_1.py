# importing packages for lab
import os
import numpy as np
import pandas as pd
from pyeeg import bin_power
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
# print(eeg_data_t.loc[:, 0])

# EEG values mean
# using axis=1 to run function across 34 channels
data_means = np.mean(eeg_data_t, axis=1)

# EEG values standard deviation
# using axis=1 to run function across 34 channels
data_sd = np.std(eeg_data_t, axis=1)

# calculating plot info
means = data_means
mean_diff = means - data_sd
mean_sum = means + data_sd

# creating scatterplot of means
# getting indicies for scatterplot x-axis
indices = list(eeg_data_t.index.values)

#plt.scatter(indices, mean_diff, color='salmon', edgecolors='salmon', label='Mean - Stddev')
#plt.scatter(indices, means, color='midnightblue', edgecolors='midnightblue', label='Means')
#plt.scatter(indices, mean_sum, color='seagreen', edgecolors='seagreen', label='Mean + Stddev')
#plt.legend()
#plt.show()

bin_powers = []

# looping over eeg_data_list to use bin_power() function
for i in eeg_data_list:
    band = [0.5, 4, 7, 12, 30]
    fs = 1024
    power = bin_power(eeg_data_t[i], band, fs)
    bin_power.append(power)

bin_powers = []
for i in range(62):
    for j in range(34):
        band = [0.5, 4, 7, 12, 30]
        fs = 1024
        psis = [bin_power(eeg_data_t.iloc[i*1024:(i+1)*1024, j], band, fs)[0][2]]
        bin_powers.append(psis)
        print(bin_powers)

psi_list = []
psi_bin = list(range(1024))
psi_list = []
for col in clmns:
    for row in range(0, len(eeg_df), 1024):
        for j in range(0, 1024):
            if row + j < len(eeg_df) - 1:
                psi_bin[j] = eeg_df[col][row + j]
                # print(eeg_df[0][row+j])
            else:
               break
        PSI_vals = pyeeg.bin_power(psi_bin, [0.5, 4, 7, 12, 30], 1024)[0][2]
        psi_list.append(PSI_vals)

print(psi_list)
len(psi_list)

# extracting alpha psi
alpha_psi = []
rows = 34

for i in range(rows):
   alphas = bin_powers[i][0][2]
   alpha_psi.append(alphas)

#plt.scatter(indices, alpha_diff, color='salmon', edgecolors='salmon', label='Mean - Stddev')
#plt.scatter(indices, a_means, color='midnightblue', edgecolors='midnightblue', label='Means')
#plt.scatter(indices, alpha_sum, color='seagreen', edgecolors='seagreen', label='Mean + Stddev')
#plt.legend()
#plt.show()

#for x in range(62):
 #   for y in range(34):
  #      psis_x = [bin_power(eeg_reshaped[x*1024:(x+1)*1024, y], band, fs)[0][2]]
   #     bin_powers.append(psis_x)
#print(np.shape(bin_powers))