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
import pandas, csv, nltk
from pmaw import PushshiftAPI

nltk.download(["names", "stopwords", "averaged_perceptron_tagger", "vader_lexicon", "punkt"])

def scrape_reddit_data(after: int, before: int, subreddits: tuple) -> None:
    """

    """
    api = PushshiftAPI()
    for i in range(len(subreddits)):
        subreddit = subreddits[i]

        posts = api.search_submissions(subreddit=subreddit, before=before, after=after,
                                       filter=['author', 'subreddit', 'title', 'selftext', 'url'])
        print(f'Retrieved {len(posts)} posts in subreddit {subreddit} from Pushshift')
        posts_df = pandas.DataFrame(posts)
        # preview the comments data
        posts_df.head(5)
        # noinspection PyTypeChecker
        posts_df.to_csv(f'data/{subreddit}_{i}.csv', header=True, index=False,
                        columns=list(posts_df.axes[1]))

def compile_text_data(filename: str) -> None:
    with open(filename) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # Read the movie review, which is the last entry in the row
        row = next(reader)
        review = row[len(row) - 1]

    return review

if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['pandas', 'pmaw', 'python_ta.contacts', 'python_ta'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': ['scrape_reddit_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
