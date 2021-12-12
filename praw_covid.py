import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()
before = int(dt.datetime(2020, 1, 1, 0, 0).timestamp())
after = int(dt.datetime(2019, 6, 1, 0, 0).timestamp())

subreddit = "depression"
limit = 100
posts = api.search_submissions(subreddit=subreddit, limit=limit, before=before, after=after)
print(f'Retrieved {len(posts)} posts from Pushshift')

posts_df = pd.DataFrame(posts)
# preview the comments data
posts_df.head(5)
posts_df.to_csv('output.csv', header=True, index=False, columns=list(posts_df.axes[1]))

