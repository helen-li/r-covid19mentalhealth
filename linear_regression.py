"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Sarah Xu & Chloe Lam.
"""

from load_global_confirmed_cases_data import read_csv_file
from load_search_term_worldwide import read_xlsx_file

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Import datasets
global_cases = read_csv_file('time_series_covid19_confirmed_global.csv')
search_interest = read_xlsx_file('search_term_worldwide.xlsx')

# Filtering both datasets so that their dates (keys) are identical
filtered_search_interest = {}
for date in search_interest:
    if date in global_cases:
        filtered_search_interest[date] = search_interest[date]

filtered_global_cases = {}
for date in filtered_search_interest:
    if date in search_interest:
        filtered_global_cases[date] = global_cases[date]


def main() -> None:
    """Fit a linear regression model to predict search term interest in 9 mental health
    related key-terms (depression, anxiety, ocd, obsessive compulsive disorder, panic attack,
    mental health, insomnia, counseling, psychiatrist) and plotting them.
    """
    x = np.array([cases for cases in filtered_global_cases.values()]).reshape((-1, 1))
    y = np.array([filtered_search_interest[key][4] for key in filtered_search_interest.keys()])  # depression

    # Create a linear regression object
    regr = LinearRegression()
    # Train the model using the data sets
    regr.fit(x, y)

    # Make predictions using globally confirmed cases
    y_pred = regr.predict(x)

    # The coefficients
    print("Coefficients: \n", regr.coef_)
    # The mean squared error
    print("Mean squared error: %.3f" % mean_squared_error(y, y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(y, y_pred))

    # Plotting original data points
    plt.scatter(x, y, color="black")
    # Plotting the linear regression model
    plt.plot(x, y_pred, color="blue", linewidth=3)

    # Labelling Axis and Title
    plt.xlabel('Globally Confirmed Covid Cases')
    plt.ylabel('Search Interest')
    plt.title('The relationship between Covid Cases and Mental Health Search Terms')

    plt.show()


if __name__ == "__main__":
    main()
