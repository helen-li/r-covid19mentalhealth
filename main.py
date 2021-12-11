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

import matplotlib

import reddit_analysis as analysis
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download the necessary nltk data resources for the project
nltk.download(['vader_lexicon', 'punkt'])

subreddits = ('depression', 'Anxiety', 'EatingDisorders', 'ForeverAlone', 'HealthAnxiety',
              'affirmations', 'helpmecope', 'itgetsbetter', 'getting_over_it', 'GetMotivated')

timestamps = [
    int(datetime.datetime(2019, 1, 1, 0, 0).timestamp()),
    int(datetime.datetime(2019, 5, 1, 0, 0).timestamp()),
    int(datetime.datetime(2020, 1, 1, 0, 0).timestamp()),
    int(datetime.datetime(2020, 5, 1, 0, 0).timestamp())
]

if __name__ == '__main__':
    # print("Scraping data from reddit...")
    # analysis.scrape_subreddit_posts(timestamps[0], timestamps[1], subreddits, 'before')
    # analysis.scrape_subreddit_posts(timestamps[2], timestamps[3], subreddits, 'after')
    # print("Reddit data has been acquired and saved as csv files in the data folder")

    for subreddit in subreddits:
        before_intensities = analysis.compile_text_data(f'data/{subreddit}_before.csv')
        after_intensities = analysis.compile_text_data(f'data/{subreddit}_after.csv')
        before_intensity = analysis.average_intensity(list(before_intensities.values()))
        after_intensity = analysis.average_intensity(list(after_intensities.values()))
        print(f'{subreddit} --- Before: {before_intensity}, After: {after_intensity}')

    # test_intensities = analysis.compile_text_data(f'data/depression_after.csv')
    # x_vals = []
    # y_vals = []
    # for timestamp in sorted(test_intensities):
    #     current_datetime = datetime.datetime.fromtimestamp(timestamp)
    #     x_vals.append(current_datetime)
    #     y_vals.append(test_intensities[timestamp])
    #
    # dates = matplotlib.dates.date2num(x_vals)
    # plt.plot_date(dates, y_vals)
    #
    # # plt.plot(x_vals, y_vals)
    # #
    # # ani = FuncAnimation(plt.gcf(), analysis.animate(before_intensities), interval=100)
    # # plt.tight_layout()
    # plt.show()

