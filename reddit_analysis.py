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
# from nltk.sentiment import SentimentIntensityAnalyzer
#
# sia = SentimentIntensityAnalyzer()

def scrape_subreddit_posts(after: int, before: int, subreddits: tuple, filename: str) -> None:
    """
    Scrapes posts from the channels given by subreddits posted during the timeframe defined
    by after and before, which are timestamps representing UTC.

    The posts data will contain 5 columns: author, timestamp, subreddit, title, and selftext.
    All scraped data will be stored in one file inside the data folder with named as filename.csv.
    """
    api = PushshiftAPI()
    posts_so_far = []

    for i in range(len(subreddits)):
        subreddit = subreddits[i]
        # parsed into a list of dictionaries mapping each filtered column to the corresponding content
        posts = api.search_submissions(subreddit=subreddit, before=before, after=after,
                                       filter=['author', 'subreddit', 'title', 'selftext'])
        print(f'Retrieved {len(posts)} posts in subreddit {subreddit} from Pushshift')
        posts_so_far = posts_so_far + posts.responses

    posts_df = pandas.DataFrame(posts_so_far)
    # noinspection PyTypeChecker
    posts_df.to_csv(f'data/{filename}.csv', header=True, index=False,
                        columns=list(posts_df.axes[1]), encoding='utf-8-sig')
#
# def compile_text_data(filename: str) -> dict[int, float]:
#     """
#     Returns a dictionary that maps timestamps to compound intensity values of posts.
#     """
#     posts_polarity_so_far = {}
#
#     with open(filename) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#
#         for row in reader:
#             # Read the post title, which is the fifth entry in the row
#             post = row[4]
#             # Add the post text, which is the third entry in the row
#             if row[2] != '[removed]':
#                 post = post + row[2]
#
#             posts_polarity_so_far[int(row[1])] = sia.polarity_scores(post)['compound']
#
#     return posts_polarity_so_far
#
# def count_words(text: str, target_word: str) -> int:
#     """
#     Counts the number of times target_word appears in text.
#
#     >>> count_words("Coronavirus is ruining my life, but I love to drink corona", "coronavirus")
#     1
#     """
#     count = 0
#     text = filter_text(text).split()
#     for word in text:
#         if target_word in word:
#             count += 1
#     return count
#
#
# def words_frequency(filename: str, words: set[str]) -> dict[str, int]:
#     """
#     Counts the frequency of target words
#     """
#     frequencies_so_far = {}
#
#     with open(filename) as file:
#         reader = csv.reader(file)
#
#         # Skip header row
#         next(reader)
#
#         for row in reader:
#             # Read the post title, which is the fifth entry in the row
#             post = row[4]
#             # Add the post text, which is the third entry in the row
#             if row[2] != '[removed]':
#                 post = post + row[2]
#
#             for word in words:
#                 if word not in frequencies_so_far:
#                     frequencies_so_far[word] = 0
#                 frequencies_so_far[word] += count_words(post, word)
#
#     return frequencies_so_far
#
#
# def filter_text(text: str) -> str:
#     """
#     Returns the lowercase version of text after filtering out any non-alphanumeric characters.
#
#     >>> filter_text('Hello, my name is Helen.')
#     'hello my name is helen'
#     """
#     text_frame = text.split(' ')
#     for i in range(len(text_frame)):
#         curr_word = text_frame[i]
#         new_word = [char.lower() for char in curr_word if char.isalnum()]
#         text_frame[i] = ''.join(new_word)
#
#     return ' '.join(text_frame)
#
#
# def word_cloud(filename: str, output_name: str) -> None:
#     """
#     Generates a word cloud based on the data provided in the file named filename.
#     """
#     df = pandas.read_csv(filename, index_col=0)
#     text = ''
#     for i in range(1, len(df.index)):
#         if not pandas.isnull(df.title[i]):
#             text = text + df.title[i]
#         if not pandas.isnull(df.selftext[i]) and df.selftext[i] != '[removed]':
#             text = text + ' ' + df.selftext[i]
#
#     stopwords = set(STOPWORDS)
#     stopwords.update(['fucking', 'fuck', 'shit', 'la', 'li', 'lu', 'le', 'lo',
#                       'will', 'want', 'people', 'life', 'im'])
#
#     wordcloud = WordCloud(stopwords=stopwords, colormap='Reds', width=1000, height=1000, mode='RGBA',
#                           background_color='white').generate(filter_text(contractions.fix(text)))
#     # plt.imshow(wordcloud, interpolation='bilinear')
#     # plt.axis("off")
#     # plt.margins(x=0, y=0)
#     # plt.show()
#     wordcloud.to_file(output_name)
#
#
def average_intensity(intensities: list[float]) -> float:
    """

    Preconditions:
      - len(intensities) > 0
    """
    return sum(intensities) / len(intensities)


if __name__ == '__main__':
    import python_ta
    # import python_ta.contracts
    #
    # python_ta.contracts.DEBUG_CONTRACTS = False
    # python_ta.contracts.check_all_contracts()
    #
    # python_ta.check_all(config={
    #     # the names (strs) of imported modules
    #     'extra-imports': ['pandas', 'pmaw', 'python_ta.contacts', 'python_ta'],
    #     # the names (strs) of functions that call print/open/input
    #     'allowed-io': ['scrape_reddit_data'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })
