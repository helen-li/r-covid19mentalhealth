""" CSC110 Project Phase 2

Loading data in csv file containing number of globally confirmed cases by date.
"""
import csv
import datetime
from typing import List


def read_csv_file(filename: str) -> dict:
    """Return the data stored in a csv file with the given filename.
    The return value is a dict mapping a date to the number of global cases that day.

    - Keys are specific dates with type datetime.date.
    - Values are the number of total cases on that date with type int.

    Preconditions:
      - file name refers to a valid csv file.
      """
    with open(filename) as file:
        reader = csv.reader(file)
        data = [process_row(row) for row in reader]
        data = add_col(data)
        return data


def process_row(row: List) -> list:
    """Removes the first 4 columns of each row, which are information about geographic location.
    Returns a list of the number of cases for one country from 1/22/20 to 12/30/21."""

    cases = []
    for i in range(4, len(row)):
        if str.isdigit(row[i]):
            cases.append(int(row[i]))
        else:
            cases.append(str_to_date(row[i]))

    return cases


def add_col(data: List[List]) -> dict:
    """Computes the total number of cases on a specific date by adding up the cells
    of each column, which is the number of cases in one country.
    Returns a dictionary mapping the date to the number of global cases."""
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
    return datetime.date(2000+int(split[2]), int(split[0]), int(split[1]))
