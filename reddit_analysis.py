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
import pandas
from pmaw import PushshiftAPI


def scrape_subreddit_posts(after: int, before: int, subreddits: tuple, filename: str) -> None:
    """
    From the channels given by the subreddits tuple, scrapes all posts that got posted during
    the timeframe defined by after and before, which are timestamps representing UTC, and then
    writes all the scraped data into a file named as filename.csv in the data folder. The csv
    file will contain 5 columns: author, timestamp, subreddit, title, and selftext (post text).
    """
    api = PushshiftAPI()
    posts_so_far = []

    for subreddit in subreddits:
        # a list of dictionaries mapping each filtered column to the corresponding content
        posts = api.search_submissions(
            subreddit=subreddit, before=before, after=after,
            filter=['author', 'created_utc', 'subreddit', 'title', 'selftext']
        )
        print(f'Retrieved {len(posts)} posts in subreddit {subreddit} from Pushshift')
        posts_so_far = posts_so_far + posts.responses

    posts_df = pandas.DataFrame(posts_so_far)
    # noinspection PyTypeChecker
    posts_df.to_csv(f'data/{filename}.csv', header=True, index=False,
                    columns=list(posts_df.axes[1]), encoding='utf-8-sig')


def average_intensity(intensities: list[float]) -> float:
    """
    Returns the average of the values in intensities if intensities is not an empty
    list; otherwise, returns 0.
    """
    if len(intensities) <= 0:
        return 0
    return sum(intensities) / len(intensities)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['pandas', 'pmaw', 'python_ta.contacts', 'python_ta'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': ['scrape_subreddit_posts'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
