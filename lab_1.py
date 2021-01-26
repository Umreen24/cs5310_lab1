import os
import numpy as np
import pandas as pd
import pyeeg
from scipy.io import loadmat

os.chdir('/Users/umreenimam/documents/masters/masters_classes/cs_5310/week_2/lab_1')
filename = 'Acquisition-15-data.mat'
data = loadmat(filename)
eeg = data['data']

eeg_data = pd.DataFrame(eeg)
eeg_data_t = eeg_data.T
print(eeg_data)
