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
import csv
import datetime
from typing import List
import pandas as pd


def read_xlsx_file(filename: str) -> dict:
    """Return the data stored in a xlsx file with the given filename.
    The return value is a dictionary mapping a date to the popularity of
    mental health-related search terms that day. The keys are specific
    dates with type datetime.date, and the values are a list of integers
    containing the number of searches for the corresponding
    mental health-related search terms on that day.

    Preconditions:
      - filename refers to a valid xlsx file.
    """
    # reading the excel file
    df = pd.read_excel(filename)
    # select first column that lists the dates
    first_column = df.iloc[:, 0]
    # dictionary to return
    dictionary = {}

    # iterate through each element in first column
    for i in range(len(first_column)):
        # we turn each element in first column to datetime.date type
        date = first_column[i].date()
        # add to dictionary. The key is the date. The value is the number of searches
        # for each respective term. Each key-value pair represents a date.
        dictionary[date] = [df.loc[i].values[j] for j in range(1, len(df.loc[i].values))]

    return dictionary


def read_csv_file(filename: str) -> dict:
    """Return the data stored in a csv file with the given filename.
    The return value is a dictionary mapping a date to the number of
    global cases that day. The keys are specific dates with type
    datetime.date, and the values are the number of total cases
    on that day with type int.

    Preconditions:
      - file name refers to a valid csv file.
    """
    with open(filename) as file:
        reader = csv.reader(file)
        data = [process_row(row) for row in reader]
        data = add_col(data)
        return data


def process_row(row: List) -> list:
    """Removes the first 4 columns of each row, which are information
    about geographic location for the files inside covid_data. Returns
    a list of the number of cases for a country from 1/22/20 to 12/30/21.
    """
    cases = []

    for i in range(4, len(row)):
        if str.isdigit(row[i]):
            cases.append(int(row[i]))
        else:
            cases.append(str_to_date(row[i]))

    return cases


def add_col(data: List[List]) -> dict:
    """Computes the total number of cases for a specific date by
    adding up the cells of each column, which each represents the
    number of cases in one country. Returns a dictionary mapping
    the date to the number of global cases."""
    final_data = {}

    for col in range(0, 344):
        total_cases = 0
        for row in range(1, 257):
            total_cases = total_cases + data[row][col]
        final_data[data[0][col]] = total_cases

    return final_data


def str_to_date(date_string: str) -> datetime.date:
    """Converts a string in mm/dd/yy format to a datetime.date.

    Preconditions:
      - date_string has format mm/dd/yy
    """
    split = str.split(date_string, '/')
    return datetime.date(2000 + int(split[2]), int(split[0]), int(split[1]))


def filter_dataset() -> list[dict]:
    """Reads data files for both global confirmed Covid cases and for worldwide
    mental health-related search terms. Filters both datasets so that their
    dates (keys in the dict) are identical and returns a list of 2 dictionaries
    representing first the search interest dataset and then the Covid cases dataset.
    """
    global_cases = read_csv_file('covid_data/time_series_covid19_confirmed_global.csv')
    search_interest = read_xlsx_file('search_terms/search_term_worldwide.xlsx')

    filtered_search_interest = {}
    for date in search_interest:
        if date in global_cases:
            filtered_search_interest[date] = search_interest[date]

    filtered_global_cases = {}
    for date in filtered_search_interest:
        if date in search_interest:
            filtered_global_cases[date] = global_cases[date]

    return [filtered_search_interest, filtered_global_cases]


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['csv', 'datetime', 'typing', 'python_ta.contacts', 'python_ta', 'pandas'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': ['read_csv_file'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
