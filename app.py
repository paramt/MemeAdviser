import praw
import pdb
import re
import os
from datetime import datetime
import time
import algorithm

template = '''This post hit #1 on [the front page](https://www.reddit.com/r/memeeconomy/hot/) within **{min}**, at **{upvotes}** upvote(s).
If you invest now, you'll break even at **{break_even}** upvotes.

&#x200B;

^(Beep boop, I'm a bot. | [Contact me](mailto://bot@param.me))
'''


reddit = praw.Reddit('MemeAdviser')

if not os.path.isfile("replied.txt"):
    replied = []
else:
    with open("replied.txt", "r") as f:
        replied = list(filter(None, f.read().split("\n")))

subreddit = reddit.subreddit("MemeEconomy")

submissions = subreddit.hot()
submission = next(submissions)

while submission.stickied:
    submission = submissions.next()

minutes = round((time.time() - submission.created_utc)/60)

if minutes >= 60:
    minutes = str(minutes//60) + "h " + str(minutes % 60) + "min"
else:
    minutes = str(round((time.time() - submission.created_utc)/60)) + " minutes"

if submission.id not in replied:
    submission.reply(template.format(upvotes=str(submission.score),
                                     time=str(datetime.utcfromtimestamp(submission.created_utc).strftime('%B %d %H:%M:%S')), min=minutes, break_even=algorithm.break_even(submission.score)))
    print("Bot replying to : ", submission.title)
    replied.append(submission.id)
    with open("replied.txt", "w") as f:
        for post_id in replied:
            f.write(post_id + "\n")
