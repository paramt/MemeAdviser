import praw
import pdb
import re
import os
from datetime import datetime
import time
import algorithm

template = '''This post hit #1 on [the front page](https://www.reddit.com/r/memeeconomy/hot/) within **{min}**, at **{upvotes}** upvotes.
If you invest now, you'll break even at **{break_even}** upvotes.

&#x200B;

^(Beep boop, I'm a bot. | [Contact me](mailto://bot@param.me))
'''

try:
    reddit = praw.Reddit('MemeAdviser')
except:
    reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'], client_secret=os.environ['CLIENT_SECRET'], password=os.environ['PASSWORD'], user_agent="MemeAdviser 0.1", username="MemeAdviser")


with open("../replied.txt", "r") as f:
    replied = list(filter(None, f.read().split("\n")))

with open("../subscribed.txt", "r") as f:
    subscribed = list(filter(None, f.read().split("\n")))

build = '0'

try:
    build = os.environ['BUILD']
except:
    pass

subreddit = reddit.subreddit("MemeEconomy")
post_subreddit = reddit.subreddit("InsiderMemeTrading")
submissions = subreddit.hot()
submission = next(submissions)

while submission.stickied:
    submission = submissions.next()

minutes = int(round((time.time() - submission.created_utc)/60))

if minutes >= 60:
    minutes = str(minutes//60) + "h " + str(minutes % 60) + "min"
else:
    minutes = str(round((time.time() - submission.created_utc)/60)) + " minutes"

if submission.id not in replied and build == '0':
    if submission.score < 800:
        post_subreddit.submit(title="This meme just hit #1 on MemeEconomy with only " + "{:,}".format(submission.score) + " upvotes! Invest now and break even at " + "{:,}".format(algorithm.break_even(submission.score)) + " upvotes", url="https://reddit.com" + submission.permalink)

    submission.reply(template.format(upvotes=str(submission.score), time=str(datetime.utcfromtimestamp(submission.created_utc).strftime('%B %d %H:%M:%S')), min=minutes, break_even=algorithm.break_even(submission.score)))

    for user in subscribed:
        reddit.redditor(user).message("MemeEconomy Update", "[This meme](https://reddit.com" + submission.permalink + ") just hit #1 on MemeEconomy with only " + "{:,}".format(submission.score) + " upvotes! Invest now and break even at " + "{:,}".format(1200) + " upvotes" + "\n\n *** \n\n ^(You're recieving this message because you've subscribed to this bot. To unsubscribe, contact u/hypnotic-hippo)")
        print("Messaging " + user)

    print("Bot replying to : ", submission.title)
    replied.append(submission.id)
    with open("../replied.txt", "w") as f:
        for post_id in replied:
            f.write(post_id + "\n")
