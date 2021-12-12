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

# Importing modules and classes
from load_global_confirmed_cases_data import read_csv_file
from load_search_term_worldwide import read_xlsx_file

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

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

# All Mental Health Search Terms in a list
mh_search_terms = ['depression', 'anxiety', 'obsessive compulsive disorder', 'ocd',
                   'insomnia', 'panic attack', 'mental health', 'counseling', 'psychiatrist']

# Plot a graph based on the search term input
def plot_graph(search_term: str):
    """Fit a linear regression model to predict search term interest in 9 mental health
    related key-terms (depression, anxiety, ocd, obsessive compulsive disorder, panic attack,
    mental health, insomnia, counseling, psychiatrist) and plotting them. """

    # Match the corresponding search_term input to mh_search_terms
    term_index = mh_search_terms.index(search_term)

    # Generate x and y values
    x = np.array([cases for cases in filtered_global_cases.values()]).reshape((-1, 1))
    y = np.array([filtered_search_interest[key][term_index] for key in filtered_search_interest.keys()])

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
    plt.ylabel(search_term)
    plt.title('The relationship between Covid Cases and ' + search_term)

    return plt.show()


# Create buttons
btns = []
for i in range(len(mh_search_terms)):
    # xposition, yposition, width, height
    axes = plt.axes([0.1, i * 0.1, 0.2, 0.1])
    btn = Button(axes, label=mh_search_terms[i], color='white', hovercolor='grey')
    btns.append(btn)

# all the possible graphs
graph_0 = plot_graph(mh_search_terms[0])
graph_1 = plot_graph(mh_search_terms[1])
graph_2 = plot_graph(mh_search_terms[2])
graph_3 = plot_graph(mh_search_terms[3])
graph_4 = plot_graph(mh_search_terms[4])
graph_5 = plot_graph(mh_search_terms[5])
graph_6 = plot_graph(mh_search_terms[6])
graph_7 = plot_graph(mh_search_terms[7])

def main() -> None:


    btns[0].on_clicked(graph_0)
    btns[1].on_clicked(graph_1)
    btns[2].on_clicked(graph_2)
    btns[3].on_clicked(graph_3)
    btns[4].on_clicked(graph_4)
    btns[5].on_clicked(graph_5)
    btns[6].on_clicked(graph_6)
    btns[7].on_clicked(graph_7)

if __name__ == "__main__":
    main()
