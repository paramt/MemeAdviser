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

if not os.path.isfile("../replied.txt"):
    replied = []
else:
    with open("../replied.txt", "r") as f:
        replied = list(filter(None, f.read().split("\n")))

if not os.path.isfile("../subscribed.txt"):
    subscribed = []
else:
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

# Find out how old the post is
minutes = int(round((time.time() - submission.created_utc)/60))

# Store time in hours
if minutes >= 60:
    minutes = str(minutes//60) + "h " + str(minutes % 60) + "min"
else:
    minutes = str(round((time.time() - submission.created_utc)/60)) + " minutes"

if submission.id not in replied and build == '0':
    # Post to r/InsiderMemeTrading
    if submission.score < 800:
        post_subreddit.submit(title="This meme just hit #1 on MemeEconomy with only " + "{:,}".format(submission.score) + " upvotes! Invest now and break even at " + "{:,}".format(algorithm.break_even(submission.score)) + " upvotes", url="https://reddit.com" + submission.permalink)

    # Send PM to subscribers
    if submission.score < 1000:
        for user in subscribed:
            reddit.redditor(user).message("MemeEconomy Update", "[This meme](https://reddit.com" + submission.permalink + ") just hit #1 on MemeEconomy with only " + "{:,}".format(submission.score) + " upvotes! Invest now and break even at " + "{:,}".format(algorithm.break_even(submission.score)) + " upvotes" + "\n\n *** \n\n ^(You're recieving this message because you've subscribed to this bot. To unsubscribe, contact u/hypnotic-hippo)")

    # Comment on r/MemeEconomy post
    submission.reply(template.format(upvotes=str(submission.score), time=str(datetime.utcfromtimestamp(submission.created_utc).strftime('%B %d %H:%M:%S')), min=minutes, break_even=algorithm.break_even(submission.score)))

    # Update replied.txt
    replied.append(submission.id)
    with open("../replied.txt", "w") as f:
        for post_id in replied:
            f.write(post_id + "\n")

# Go through each unread message
for message in reddit.inbox.unread():

    # Check for new unsubscriptions
    if re.search("unsubscribe", message.body, re.IGNORECASE) or re.search("unsubscribe", message.subject, re.IGNORECASE):
        if message.author.name in subscribed:
            subscribed.remove(message.author.name)
            with open("../subscribed.txt", "w") as f:
                for user in subscribed:
                    f.write(user + "\n")
            message.reply("You've unsubscribed from MemeAdviser! To subscribe, reply with 'Subscribe'")
        else:
            message.reply("You aren't subscribed to MemeAdviser! If you want to subscribe, reply with 'Subscribe'")

    # Check for new subscriptions
    elif re.search("subscribe", message.body, re.IGNORECASE) or re.search("subscribe", message.subject, re.IGNORECASE):
        if message.author.name not in subscribed:
            subscribed.append(message.author.name)
            with open("../subscribed.txt", "w") as f:
                for user in subscribed:
                    f.write(user + "\n")
            message.reply("You've subscribed to MemeAdviser! To unsubscribe, reply with 'Unsubscribe'")
        else:
            message.reply("You're already subscribed to MemeAdviser! If you want to unsubscribe, reply with 'Unsubscribe'")


# Mark all messages as read
unread_messages = []
for item in reddit.inbox.unread(limit=None):
    unread_messages.append(item)
reddit.inbox.mark_read(unread_messages)
