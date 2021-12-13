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
from dataclasses import dataclass
import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import process_text

STOPWORDS = {
    "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an",
    "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot",
    "could", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get",
    "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i",
    "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may",
    "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often",
    "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should",
    "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what",
    "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet",
    "you", "your", "fucking", "fuck", "shit", 'want', 'people', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine', 'ten', 'life', 'im', 'thing', 'ill', 'something',
    'actually', 'dont', 'really', 'ive', 'didnt', 'cant', 'id', 'thats', 'etc', 'now', 'things',
    'know', 'think', 'feel', 'anyone', 'maybe', 'even', 'thought', 'thoughts', 'one', 'probably',
    'sometime', 'sometimes', 'still', 'being', 'always', 'alway', 'someone', 'up', 'person',
    'everything', 'going', 'here', 'out', 'usually', 'through', 'seem', 'er', 'very', 'anything',
    'anyway', 'theres', 'wanna', 'literally', 'doesnt', 'though'
}


@dataclass
class RedditPost:
    """A post made by a user on Reddit.

    Instance Attributes:
      - name: the name of the user who created the post
      - time: the timestamp when the post was created
      - subreddit: the subreddit channel the post is in
      - title: the title of the post as a list of sentences
      - text: the body of the post as a list of sentences

    Representation Invariants:
      - self.name != ''
      - self.subreddit != ''
      - text != ['[removed]']

    Sample Usage:
    >>> post = RedditPost(name='GoldWhale', timestamp=1548391541, subreddit='depression',\
                title=['I have no motivation and I need to vent because I have lost control.'],\
                text=['I want to be healthier', 'I want to be more engaged'])
    """
    name: str
    timestamp: int
    subreddit: str
    title: list[str]
    text: list[str]


class Subreddit:
    """
    A subreddit channel with posts.
    """
    # Private Instance Attributes:
    #   - channel: the name of the subreddit channel
    #   - posts: the posts made in the relevant subreddit
    _channel: str
    _posts: list[RedditPost]

    def __init__(self, channel: str, filename: str) -> None:
        """
        Initialize a new subreddit channel.

        The channel starts by reading a file with data about posts.
        """
        self._channel = channel
        self._posts = []

        with open(filename) as file:
            reader = csv.reader(file)

            # Skip header row
            next(reader)

            for row in reader:
                subreddit = row[3]
                # Checks that the post is in the correct subreddit channel
                if subreddit == channel:
                    author = row[0]
                    created_utc = int(row[1])
                    selftext = row[2]
                    if selftext == '[removed]':
                        selftext = ''
                    selftext = nltk.tokenize.sent_tokenize(selftext)
                    title = nltk.tokenize.sent_tokenize(row[4])
                    self._posts.append(RedditPost(name=author, timestamp=created_utc,
                                                  subreddit=subreddit, title=title, text=selftext))

    def words_frequency(self, keywords: set[str]) -> dict[str, int]:
        """
        Counts the frequency of words in the posts in this subreddit and returns
        a dictionary mapping each keyword to its corresponding count.
        """
        frequencies_so_far = {}

        for post in self._posts:
            for keyword in keywords:
                if keyword not in frequencies_so_far:
                    frequencies_so_far[keyword] = 0

                count = 0
                for sentence in post.title + post.text:
                    count += process_text.count_words(sentence, keyword)

                frequencies_so_far[keyword] += count

        return frequencies_so_far

    def intensity_analysis(self) -> dict[int, float]:
        """
        Returns a dictionary that maps timestamps to compound intensity values of posts.
        """
        sia = SentimentIntensityAnalyzer()
        posts_intensity_so_far = {}

        for post in self._posts:
            sentences = post.title + post.text
            intensity_so_far = []
            for sentence in sentences:
                intensity_so_far.append(sia.polarity_scores(sentence)['compound'])
            if len(intensity_so_far) > 0:
                posts_intensity_so_far[post.timestamp] = \
                    sum(intensity_so_far) / len(intensity_so_far)

        return posts_intensity_so_far

    def word_cloud(self, output_file: str) -> None:
        """
        Generates a word cloud and stores the output image in a file named output_file.
        """
        text = ''
        for post in self._posts:
            text = text + ' '.join(post.title) + ' ' + ' '.join(post.text)

        wordcloud = WordCloud(stopwords=STOPWORDS, colormap='Reds',
                              width=1000, height=1000, mode='RGBA',
                              background_color='white').generate(process_text.filter_text(text))
        wordcloud.to_file(output_file)


def polarity_analysis(intensities: dict[int, float]) -> dict[str, int]:
    """
    Returns the number of positive, negative, and neutral posts based intensity values
    passed in from intensities.
    """
    pos, neg, neu = 0, 0, 0

    for timestamp in intensities:
        if intensities[timestamp] >= 0.05:
            pos += 1
        elif intensities[timestamp] <= -0.05:
            neg += 1
        else:
            neu += 1

    return {'positive': pos, 'negative': neg, 'neutral': neu}


def average_intensity(intensities: list[float]) -> float:
    """
    Returns the average of the values in intensities if intensities is not an empty
    list; otherwise, returns 0.

    >>> average_intensity([3.4, 5.2, 9.0, 2.4])
    5.0
    >>> average_intensity([])
    0
    """
    if len(intensities) <= 0:
        return 0
    return sum(intensities) / len(intensities)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    import doctest

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        # the names (strs) of imported modules
        'extra-imports': ['dataclasses', 'csv', 'nltk', 'nltk.sentiment', 'wordcloud',
                          'process_text', 'python_ta.contacts', 'python_ta', 'doctest'],
        # the names (strs) of functions that call print/open/input
        'allowed-io': ['__init__'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
