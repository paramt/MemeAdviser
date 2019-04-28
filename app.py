import praw
import re
from datetime import datetime
import time
import algorithm

comment_message = '''I **strongly advise** investing! This meme hit #1 on [hot](https://www.reddit.com/r/memeeconomy/hot/) within **{min}**, at **{upvotes}** upvotes. If you invest now, you'll break even at **{break_even}** upvotes.

[Click here](https://www.param.me/meme/calculator/break-even) to calculate the current break-even point. [Click here](https://www.reddit.com/message/compose?to=MemeAdviser&subject=Subscribe&message=Subscribe) to subscribe to daily market updates.

*****

^(Beep boop, I'm a bot | [Contact me](mailto://bot@param.me))
'''

submission_message = "This meme just hit #1 on MemeEconomy with only {upvotes} upvotes! Invest now and break even at {break_even} upvotes"

update_message = '''[This meme](https://reddit.com{link}) just hit #1 on MemeEconomy with only {upvotes} upvotes! Invest now and break even at {break_even} upvotes

***

^(You're recieving this message because you've subscribed to this bot. To unsubscribe, reply 'Unsubscribe')
'''

reddit = praw.Reddit('MemeAdviser')

with open("../replied.txt", "r") as f:
    replied = list(filter(None, f.read().split("\n")))

with open("../subscribed.txt", "r") as f:
    subscribed = list(filter(None, f.read().split("\n")))

subreddit = reddit.subreddit("MemeEconomy")
post_subreddit = reddit.subreddit("InsiderMemeTrading")
submissions = subreddit.hot()
submission = next(submissions)

while submission.stickied:
    submission = submissions.next()

# Find out how old the post is
minutes = int(round((time.time() - submission.created_utc) / 60))

# Store time in hours
if minutes >= 60:
    minutes = str(minutes // 60) + "h " + str(minutes % 60) + "min"
else:
    minutes = str(round((time.time() - submission.created_utc) / 60)) + " minutes"

if submission.id not in replied:
    try:
        # Update replied.txt
        replied.append(submission.id)
        with open("../replied.txt", "w") as f:
            for post_id in replied:
                f.write(post_id + "\n")

        # Post to r/InsiderMemeTrading
        if submission.score < 800:
            post_subreddit.submit(title=submission_message.format(upvotes=submission.score, break_even=algorithm.break_even(submission.score)), url="https://reddit.com" + submission.permalink)

        # Send PM to subscribers
        if submission.score < 1000:
            for user in subscribed:
                reddit.redditor(user).message("MemeEconomy Update", update_message.format(link=submission.permalink, upvotes=submission.score, break_even=algorithm.break_even(submission.score)))

        # Comment on r/MemeEconomy post
        if submission.score < 1000:
            submission.reply(comment_message.format(upvotes=str(submission.score), time=str(datetime.utcfromtimestamp(submission.created_utc).strftime('%B %d %H:%M:%S')), min=minutes, break_even=algorithm.break_even(submission.score)))

    except:
        pass

unread_messages = []

# Go through each unread message
for message in reddit.inbox.unread():
    unread_messages.append(message)

    # Check for new unsubscriptions
    if re.search("unsubscribe", message.body, re.IGNORECASE) or re.search("unsubscribe", message.subject, re.IGNORECASE):
        if message.author.name in subscribed:
            subscribed.remove(message.author.name)
            with open("../subscribed.txt", "w") as f:
                for user in subscribed:
                    f.write(user + "\n")
            message.reply("You've unsubscribed from MemeAdviser. To subscribe, reply with 'Subscribe'")
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
reddit.inbox.mark_read(unread_messages)
