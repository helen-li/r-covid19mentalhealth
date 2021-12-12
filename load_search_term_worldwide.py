""" CSC110 Project Phase 2

Loading data in xlsx file containing number of searches of mental health terms by date.
"""
# importing modules
import pandas as pd


def read_xlsx_file(filename: str) -> dict:
    """Return the data stored in a xlsx file with the given filename.
    The return value is a dict mapping a date to the number of global cases that day.

    - Keys are specific dates with type datetime.date.
    - Values are a list of integers containing the number of searches of the corresponding
        mental health search terms on that date.

    Preconditions:
    - file name refers to a valid xlsx file.
    """
    # reading the excel file
    df = pd.read_excel(filename)
    # select first column that lists the dates
    first_column = df.iloc[:, 0]

    # dictionary to return.
    dictionary = {}

    # iterate through each element in first_column
    for i in range(len(first_column)):
        # we turn each element in first column to datetime.date type
        date = first_column[i].date()
        # add to dictionary. The key is the date. The value is the number of searches
        # for each respective term. Each key-value pair represents a date.
        dictionary[date] = [df.loc[i].values[j] for j in range(1, len(df.loc[i].values))]

    return dictionary
