"""Linear regression model"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from load_global_confirmed_cases_data import read_csv_file
import datetime

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

global_cases = read_csv_file('time_series_covid19_confirmed_global.csv')
search_interest = {datetime.date(19, 12, 1): [50, 60], datetime.date(19, 12, 20): [60, 70],
                   datetime.date(20, 1, 5): [75, 85], datetime.date(20, 1, 20): [80, 88],
                   datetime.date(20, 2, 10): [82, 90], datetime.date(20, 3, 10): [80, 88],
                   datetime.date(20, 4, 10): [60, 88], datetime.date(20, 5, 10): [100, 92],
                   datetime.date(20, 5, 28): [78, 99], datetime.date(20, 6, 19): [92, 90],
                   datetime.date(20, 7, 28): [75, 85], datetime.date(20, 8, 19): [66, 83]}
# 12 test cases
i = 0
test_cases = []
for cases in global_cases.values():
    if i < 12:
        test_cases.append(cases)
    i += 1
[0, 1, 2, 3]
[3, 4, 5, 6]
x = np.array(test_cases).reshape((-1, 1))
y = np.array([search_interest[key][0] for key in search_interest.keys()])
regr = LinearRegression()
# for visualisation
plt.scatter(x, y, color='b')
plt.plot(x, y, color='k')
# for calculating coefficient and intercept values
regr.fit(x, y)
# print(regr.score(x, y))
# plt.plot(x, y, color='b')
# plt.show()
# from pydataset import data
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from matplotlib import pyplot as pit
#
# # %matplotlib notebook
#
# pima = data('Pima.tr')
# Problem: The x and y variable have to be one-to-one (i.e. the first value in x and first value in y
# are information from the same date. So the number of x and y values have to match, which leaves us
# with 19 points (amount of overlap in dates there is between the 2 datasets). too little?
