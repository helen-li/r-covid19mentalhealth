"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Helen Li.
"""
import datetime

from lin_regression import plot_linear_regression_graph

if __name__ == '__main__':

    timestamps = [
        int(datetime.datetime(2019, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2019, 4, 30, 0, 0).timestamp()),
        int(datetime.datetime(2020, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2020, 4, 30, 0, 0).timestamp())
    ]

    # Plots the line graphs
    # plot_line_graphs()
    plot_linear_regression_graph()


