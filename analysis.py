
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import random

salaries = pd.read_csv('Salaries.csv',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
salaries.info()

for col in ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits']:
    salaries[col] = pd.to_numeric(salaries[col], errors='coerce')

salaries = salaries.drop('Notes', axis=1)
    
salaries.describe()

sns.set_style("whitegrid")

x = [np.random.uniform(100) for _ in range(200)]
y = [np.random.uniform(100) for _ in range(200)]
plt.scatter(x,y)
plt.show()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)

ax2.scatter(*[[np.random.normal(100) for i in range(100)] for i in range(2)])


fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50).cumsum(), 'k--')


ax2 = fig.add_subplot(1,2,2)           
ax2.plot(np.random.randn(50).cumsum(), 'r--')
