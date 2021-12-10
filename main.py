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
import reddit_analysis as analysis

subreddits = ('depression', 'Anxiety')
time_1 = int(datetime.datetime(2019, 1, 1, 0, 0).timestamp())
time_2 = int(datetime.datetime(2019, 4, 1, 0, 0).timestamp())
# time_3 = int(datetime.datetime(2020, 1, 1, 0, 0).timestamp())
# time_4 = int(datetime.datetime(2020, 4, 1, 0, 0).timestamp())

if __name__ == '__main__':
    print("Scraping data from reddit...")
    analysis.scrape_reddit_data(time_1, time_2, subreddits)
    # analysis.scrape_reddit_data(time_3, time_4, subreddits)
    print("Reddit data has been acquired and saved as csv files in the data folder")

