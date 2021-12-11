"""
CSC110 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
import csv


def read_csv_file(filename: str) -> dict:
    """
    Return a dictionary with the first element being the list of weeks and the remaining elements
    mapping the country name to the list of numbers representing the search interest of mental
    health related terms based on the data in filename.

    The keys represent the names of the countries as strings.
    The values of the first list are strings of dates representing the weeks from 2019/06/16 to
    2020/05/31 and the values of the remaining lists represent the number of online Google searches
    for mental health related terms as integers from 0 through to 100 in order of popularity.

    Preconditions:
      - filename refers to a valid csv file
    """
    weeks = []
    japan = []
    italy = []
    canada = []
    iran = []
    uk = []
    sk = []
    us = []

    search_term_interest = {}

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)

        for row in reader:
            weeks.append(row[0])
            japan.append(int(row[1]))
            italy.append(int(row[2]))
            canada.append(int(row[3]))
            iran.append(int(row[4]))
            uk.append(int(row[5]))
            sk.append(int(row[6]))
            us.append(int(row[7]))

        search_term_interest['week'] = weeks
        search_term_interest['japan'] = japan
        search_term_interest['italy'] = italy
        search_term_interest['canada'] = canada
        search_term_interest['iran'] = iran
        search_term_interest['uk'] = uk
        search_term_interest['south_korea'] = sk
        search_term_interest['us'] = us

        return search_term_interest
