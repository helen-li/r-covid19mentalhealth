""" CSC110 Project Phase 2

Loading data in xlsx file containing number of searches of mental health terms by date.
"""
# importing modules
import pandas as pd

# reading the excel file
df = pd.read_excel("data\search_term_worldwide.xlsx")
# select first column that lists the dates
first_column = df.iloc[:, 0]
list_first_column = [item for item in first_column]

# dictionary to return.
dictionary = {}

# iterate through each element in first column
for i in range(len(first_column)):
    # we turn each element in first column to datetime.date type
    date = first_column[i].date()
    # add to dictionary.
    # The key is the date.
    # The value is the number of searches for each respective term.
    # Each key-value pair represents a date.
    dictionary[date] = [df.loc[i].values[j] for j in range(1, len(df.loc[i].values))]

print(dictionary)
