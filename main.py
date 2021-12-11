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
import datetime, nltk, ssl
import reddit_analysis as analysis

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download(['vader_lexicon', 'punkt'])

subreddits = ('depression', 'affirmations')

time_1 = int(datetime.datetime(2019, 1, 1, 0, 0).timestamp())
time_2 = int(datetime.datetime(2019, 3, 1, 0, 0).timestamp())
time_3 = int(datetime.datetime(2020, 1, 1, 0, 0).timestamp())
time_4 = int(datetime.datetime(2020, 3, 1, 0, 0).timestamp())

if __name__ == '__main__':
    # print("Scraping data from reddit...")
    # analysis.scrape_subreddit_posts(time_1, time_2, subreddits, 'before')
    # analysis.scrape_subreddit_posts(time_3, time_4, subreddits, 'after')
    # print("Reddit data has been acquired and saved as csv files in the data folder")

    for subreddit in subreddits:
        before_intensities = analysis.compile_text_data(f'data/{subreddit}_before.csv')
        after_intensities = analysis.compile_text_data(f'data/{subreddit}_after.csv')
        before_intensity = analysis.average_intensity(list(before_intensities.values()))
        after_intensity = analysis.average_intensity(list(after_intensities.values()))
        print(f'{subreddit} --- Before: {before_intensity}, After: {after_intensity}')

