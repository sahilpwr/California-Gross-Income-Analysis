
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import random
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


# first checkout the data
salaries = pd.read_csv('Salaries.csv',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
salaries.info()

for col in ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits']:
    salaries[col] = pd.to_numeric(salaries[col], errors='coerce')

salaries = salaries.drop('Notes', axis=1)
    
salaries.describe()

# i am using seaborn to change aesthetics of the plots
sns.set_style("whitegrid")

# matplotlib.pyplot is the main module that provides the plotting API
x = [np.random.uniform(100) for _ in range(200)]
y = [np.random.uniform(100) for _ in range(200)]
plt.scatter(x,y)
plt.show()

# add_subplot returns the axis object that you can reference
# and manipulate

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)

ax2.scatter(*[[np.random.normal(100) for i in range(100)] for i in range(2)])


# instead you have to run the sequence of commands in one cell

# create the figure to hold the subplots
fig = plt.figure()

# add a subplot     row, col, selected plot for reference
# i will be using one row that contains two plots
ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50).cumsum(), 'k--')

# same as before
ax2 = fig.add_subplot(1,2,2)           # this indicates color and line style
ax2.plot(np.random.randn(50).cumsum(), 'r--')
