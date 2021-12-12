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
import nltk
import ssl
import reddit_analysis as analysis
import post


if __name__ == '__main__':

    # Ensure a smooth process of downloading
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # Download the necessary nltk data resources for the project
    nltk.download(['vader_lexicon', 'punkt'])

    # Store the relevant subreddits in a tuple structure
    subreddits = ('depression', 'Anxiety', 'OCD', 'insomnia', 'PanicAttack',
                  'mentalhealth', 'counselling', 'Psychiatry')

    timestamps = [
        int(datetime.datetime(2019, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2019, 4, 30, 0, 0).timestamp()),
        int(datetime.datetime(2020, 1, 1, 0, 0).timestamp()),
        int(datetime.datetime(2020, 4, 30, 0, 0).timestamp())
    ]

    # Scraping posts data from the relevant subreddits
    print("Scraping data from reddit...")
    analysis.scrape_subreddit_posts(timestamps[0], timestamps[1], subreddits, 'before')
    print("Completed for the first given timeframe...")
    analysis.scrape_subreddit_posts(timestamps[2], timestamps[3], subreddits, 'after')
    print("Reddit data has been acquired and saved as csv files inside the data folder")

    # Perform sentiment analysis and generate word clouds using the scraped data
    for subreddit in subreddits:
        before_channel = post.Subreddit(subreddit, f'data/before.csv')
        after_channel = post.Subreddit(subreddit, f'data/after.csv')

        before_intensities = before_channel.intensity_analysis()
        before_polarities = post.polarity_analysis(before_intensities)

        after_intensities = after_channel.intensity_analysis()
        after_polarities = post.polarity_analysis(after_intensities)

        before_intensity = analysis.average_intensity(list(before_intensities.values()))
        after_intensity = analysis.average_intensity(list(after_intensities.values()))

        print(f'{subreddit} --- Before: {before_intensity}, After: {after_intensity}')
        print(f'{subreddit} --- Before: {before_polarities}, After: {after_polarities}')

        print(f'Generating word clouds for {subreddit}...')
        before_channel.word_cloud(f'img/{subreddit}_before.png')
        after_channel.word_cloud(f'img/{subreddit}_after.png')
        print(f'Word clouds generated for {subreddit}!')
