"""Linear regression model"""

from sklearn.linear_model import LinearRegression
from load_global_confirmed_cases_data import read_csv_file
from load_search_term_worldwide import read_xlsx_file

import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

global_cases = read_csv_file('time_series_covid19_confirmed_global.csv')
search_interest = read_xlsx_file('search_term_worldwide.xlsx')

# filtereing search interest dataset so the dates are the ones that overlap w global_cases
filtered_search_interest = {}
for date in search_interest:
    if date in global_cases:
        filtered_search_interest[date] = search_interest[date]

# filtering global cases according to filtered_search_interest
filtered_global_cases = {}
for date in filtered_search_interest:
    if date in search_interest:
        filtered_global_cases[date] = global_cases[date]

#
def main():
    """ hi """
    # observations / data
    x = np.array([cases for cases in filtered_global_cases.values()]).reshape((-1, 1))
    y = np.array([filtered_search_interest[key][3] for key in filtered_search_interest.keys()])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)

x = np.array([cases for cases in filtered_global_cases.values()]).reshape((-1, 1))
y = np.array([filtered_search_interest[key][3] for key in filtered_search_interest.keys()])  # depression
# 3 ocd increased, 6 mental health (not rly)
# 7 counselling went down
# 4 insomnia, 5 panic attack, 0 depression, up and down
# 8 psychiatrist - idk

# for visualisation
# for calculating coefficient and intercept values
# regr = LinearRegression()
# #
# plt.show()
# regr.fit(x, y)
# print(regr.score(x, y))
#
# y_pred = regr.predict(x)
# plt.scatter(x, y, color='b')
# plt.xlabel('Covid Cases')
# plt.ylabel('Search Interest')
# plt.title('The relationship between Covid Cases and Mental Health Search Terms')
# plt.show()

# Problem: The x and y variable have to be one-to-one (i.e. the first value in x and first value in y
# are information from the same date. So the number of x and y values have to match, which leaves us
# with 19 points (amount of overlap in dates there is between the 2 datasets). too little?


def estimate_coef(x, y) -> tuple:
    """ hi """
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b) -> None:
    """ hi """
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=20)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('Covid Cases')
    plt.ylabel('Search Interest')
    plt.title('The relationship between Covid Cases and Mental Health Search Terms')

    # restricting range of y-axis
    plt.ylim([40, 110])

    # function to show plot
    plt.show()


if __name__ == "__main__":
    main()

