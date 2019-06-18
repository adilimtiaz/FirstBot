import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

for post in subreddit.hot(limit=5):
    print("Title: ", post.title)
    print("Text: ", post.selftext)
    print("Score: ", post.score)
    print("---------------------------------\n")