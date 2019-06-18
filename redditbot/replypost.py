import praw
import pdb
import re
import os

# Create Reddit instance
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    # Open txt file with all previously replied to posts
    with open("posts_replied_to.txt", "r") as file:
        posts_replied_to = file.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for post in subreddit.hot(limit=5):
    if post.id not in posts_replied_to:
        if re.search("i don't know python", post.title, re.IGNORECASE):
            post.reply("you sure?")
            print("Bot replying to: ", post.title)
            posts_replied_to.append(post.id)

    # Write updated list back to file
with open("posts_replied_to.txt", "w") as file:
    for post_id in posts_replied_to:
        file.write(post_id + "\n")
