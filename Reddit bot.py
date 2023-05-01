import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv('client_id'),
    client_secret=os.getenv('client_secret'),
    username=os.getenv('username'),
    password=os.getenv('password'),
    user_agent="<wysiBot1.0>"
)

subreddit = reddit.subreddit("all")
for comment in subreddit.stream.comments(skip_existing=True):
    if "727" in comment.body:
        print(comment.body)
        comment.reply("WYSI")
