"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Asma Jaseem, Helen Li, Chloe Lam, Sarah Yi.
"""
import datetime
import nltk
import ssl
from reddit_scrape import scrape_subreddit_posts as scrape
import post
from display_line_graphs import plot_line_graphs
# from lin_regression import plot_linear_regression_graph

if __name__ == '__main__':
    # Ensure a smooth process of downloading required data resources for nltk to function
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # Download the necessary nltk data resources for the project
    nltk.download(['vader_lexicon', 'punkt'])

    # Store the relevant subreddits
    subreddits = ('depression', 'Anxiety', 'OCD', 'insomnia', 'PanicAttack',
                  'mentalhealth', 'counselling', 'Psychiatry')

    # Edit this set if needed to search for the frequency of these terms in subreddits
    covid_terms = {'coronavirus'}

    timestamps = [
        int(datetime.datetime(2019, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2019, 4, 30, 0, 0).timestamp()),
        int(datetime.datetime(2020, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2020, 4, 30, 0, 0).timestamp())
    ]

    # Plots the line graphs
    plot_line_graphs()

    # Plots the linear regression models
    # plot_linear_regression_graph()

    # Scraping posts data from the relevant subreddits
    print("Scraping data from reddit...")
    scrape(timestamps[0], timestamps[1], subreddits, 'before')
    print("Completed for the first given timeframe...")
    scrape(timestamps[2], timestamps[3], subreddits, 'after')
    print("Reddit data has been acquired and saved as csv files inside the data folder")

    # Perform sentiment analysis and generate word clouds using the scraped data
    for subreddit in subreddits:
        before_channel = post.Subreddit(subreddit, f'data/before.csv')
        after_channel = post.Subreddit(subreddit, f'data/after.csv')

        before_intensities = before_channel.intensity_analysis()
        before_polarities = post.polarity_analysis(before_intensities)
        before_intensity = post.average_intensity(list(before_intensities.values()))

        after_intensities = after_channel.intensity_analysis()
        after_polarities = post.polarity_analysis(after_intensities)
        after_intensity = post.average_intensity(list(after_intensities.values()))
        after_frequency = after_channel.words_frequency(covid_terms)

        print(f'----- r/{subreddit} ----- \n'
              f'::::: Intensity values ::::: \n'
              f'Before: {before_intensity}, After: {after_intensity} \n'
              f'::::: Polarity values ::::: \n'
              f'Before: {before_polarities}, After: {after_polarities} \n'
              f'::::: Frequency of {covid_terms} in r/{subreddit} ::::: \n'
              f'After: {after_frequency}')

        print(f'----- Word clouds coming for r/{subreddit} ----- \n')
        print(f'Generating the first word cloud for subreddit r/{subreddit}...')
        before_channel.word_cloud(f'img/{subreddit}_before.png')
        print(f'Generating the second word cloud for subreddit r/{subreddit}...')
        after_channel.word_cloud(f'img/{subreddit}_after.png')
        print(f'Word clouds generated for subreddit r/{subreddit}!')
