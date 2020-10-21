import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('测试(1).xls')

raw_label = data.iloc[6:, 0]

first_col = data.iloc[6:, 1]
print(first_col)