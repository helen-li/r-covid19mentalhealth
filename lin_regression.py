"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Sarah Xu, Chloe Lam, Helen Li.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from load_regression_data import filter_dataset

# Import filtered datasets
FILTERED_SEARCH_INTEREST, FILTERED_GLOBAL_CASES = filter_dataset()

# All relevant mental health-related search terms in a list
MH_SEARCH_TERMS = ['depression', 'anxiety', 'obsessive compulsive disorder', 'ocd',
                   'insomnia', 'panic attack', 'mental health', 'counseling', 'psychiatrist']


def plot_graph(search_term: str) -> plt.show():
    """Fits a linear regression model for the relationship between
    global confirmed Covid cases and interest in search_term on Google.
    Returns the resulting plot to help predict search_term interest.

    Preconditions:
      - search_term in MH_SEARCH_TERMS
    """

    # Match the corresponding search_term input to mh_search_terms
    term_index = MH_SEARCH_TERMS.index(search_term)

    # Generate x and y values
    x = np.array(list(FILTERED_GLOBAL_CASES.values())).reshape((-1, 1))
    y = np.array([FILTERED_SEARCH_INTEREST[key][term_index] for key in
                  FILTERED_SEARCH_INTEREST])

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

    _, ax = plt.subplots()

    plt.subplots_adjust(bottom=0.25)

    # Plotting original data points
    plt.scatter(x, y, linewidth=2, color="black")
    # Plotting the linear regression model
    plt.plot(x, y_pred, color="blue", linewidth=3)

    # Labelling Axis and Title
    ax.set(xlabel='Globally Confirmed Covid Cases', ylabel="Search Interest for " + search_term,
           title='Confirmed COVID-19 Cases vs. Seach Interest for ' + search_term)

    return plt.show()


# all the possible regression functions
def graph_depression(event: str) -> None:
    """Plots graph for search term "depression"."""
    plot_graph(MH_SEARCH_TERMS[0])
    plt.draw()


def graph_anxiety(event: str) -> None:
    """Plots graph for search term "anxiety"."""
    plot_graph(MH_SEARCH_TERMS[1])
    plt.draw()


def graph_ocd_1(event: str) -> None:
    """Plots graph for search term "obsessive compulsive disorder"."""
    plot_graph(MH_SEARCH_TERMS[2])
    plt.draw()


def graph_ocd_2(event: str) -> None:
    """Plots graph for search term "ocd"."""
    plot_graph(MH_SEARCH_TERMS[3])
    plt.draw()


def graph_insomnia(event: str) -> None:
    """Plots graph for search term "insomnia"."""
    plot_graph(MH_SEARCH_TERMS[4])
    plt.draw()


def graph_panic_attack(event: str) -> None:
    """Plots graph for search term "panic attack"."""
    plot_graph(MH_SEARCH_TERMS[5])
    plt.draw()


def graph_mental_health(event: str) -> None:
    """Plots graph for search term "mental health"."""
    plot_graph(MH_SEARCH_TERMS[6])
    plt.draw()


def graph_counseling(event: str) -> None:
    """Plots graph for search term "counseling"."""
    plot_graph(MH_SEARCH_TERMS[7])
    plt.draw()


def graph_psychiatrist(event: str) -> None:
    """Plots graph for search term "psychiatrist"."""
    plot_graph(MH_SEARCH_TERMS[8])
    plt.draw()


def plot_linear_regression_graph(btns: list[Button]) -> None:
    """Plots interactive linear regression models with the help
     of matplotlib Button widgets passed into the function.
    """
    btns[0].on_clicked(graph_depression)
    btns[1].on_clicked(graph_anxiety)
    btns[2].on_clicked(graph_ocd_1)
    btns[3].on_clicked(graph_ocd_2)
    btns[4].on_clicked(graph_insomnia)
    btns[5].on_clicked(graph_panic_attack)
    btns[6].on_clicked(graph_mental_health)
    btns[7].on_clicked(graph_counseling)
    btns[8].on_clicked(graph_psychiatrist)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['numpy', 'matplotlib.pyplot', 'matplotlib.widgets',
                          'sklearn.linear_model', 'sklearn.metrics',
                          'oad_regression_data', 'python_ta.contacts', 'python_ta'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': ['read_csv_file', 'plot_graph'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
