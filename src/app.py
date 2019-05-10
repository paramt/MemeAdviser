from datetime import datetime
import os
import re
import time as t
import praw

from src import algorithm
from src import constants

def main(usePreset: bool, thresholds=constants.Thresholds):

	if(usePreset):
		reddit = praw.Reddit('MemeAdviser')
	else:
		reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
                             client_secret=os.environ['CLIENT_SECRET'],
                             user_agent=os.environ['USER_AGENT'])

	with open("../data/replied.txt", "r") as f:
		replied = f.read().splitlines()

	with open("../data/subscribed.txt", "r") as f:
		subscribed = f.read().splitlines()

	subreddit = reddit.subreddit("MemeEconomy")
	submissions = subreddit.hot()

	# Find the top submission that isn't stickied
	submission = next(submissions)

	while submission.stickied:
		submission = submissions.next()

	# Find out how old the submission is
	time = int(round((t.time() - submission.created_utc) / 60))

	if time >= 60:
		time = str(time // 60) + "h " + str(time % 60) + "min"
	else:
		time = str(round((time.time() - submission.created_utc) / 60)) + " time"

	if submission.id not in replied:
		try:
			# Update replied.txt
			replied.append(submission.id)
			with open("../data/replied.txt", "w") as f:
				for post_id in replied:
					f.write(post_id + "\n")
		except IOError as e:
			print("IOError:")
			print(e)

		try:
			# Post to r/InsiderMemeTrading
			if submission.score < thresholds.submission:
				reddit.subreddit("InsiderMemeTrading").submit(title=constants.Messages.submission.format(upvotes=submission.score, break_even=algorithm.break_even(submission.score)), url="https://reddit.com" + submission.permalink)

			# Send PM to subscribers
			if submission.score < thresholds.pm:
				for user in subscribed:
					reddit.redditor(user).message("MemeEconomy Update", constants.Messages.pm.format(link=submission.permalink, upvotes=submission.score, break_even=algorithm.break_even(submission.score)))

			# Comment on r/MemeEconomy post
			if submission.score < thresholds.comment:
				submission.reply(constants.Messages.comment.format(upvotes=str(submission.score), time=time, break_even=algorithm.break_even(submission.score)))

		except praw.exceptions.PRAWException as e:
			print("PRAW Error:")
			print(e)

	unread_messages = []

	# Go through each unread message
	for message in reddit.inbox.unread():
		unread_messages.append(message)

		# Check for new unsubscriptions
		if re.search("unsubscribe", message.body, re.IGNORECASE) or re.search("unsubscribe", message.subject, re.IGNORECASE):
			if message.author.name in subscribed:
				subscribed.remove(message.author.name)
				with open("../data/subscribed.txt", "w") as f:
					for user in subscribed:
						f.write(user + "\n")
				message.reply("You've unsubscribed from MemeAdviser. To subscribe, reply with 'Subscribe'")
			else:
				message.reply("You aren't subscribed to MemeAdviser! If you want to subscribe, reply with 'Subscribe'")

		# Check for new subscriptions
		elif re.search("subscribe", message.body, re.IGNORECASE) or re.search("subscribe", message.subject, re.IGNORECASE):
			if message.author.name not in subscribed:
				subscribed.append(message.author.name)
				with open("../data/subscribed.txt", "w") as f:
					for user in subscribed:
						f.write(user + "\n")
				message.reply("You've subscribed to MemeAdviser! To unsubscribe, reply with 'Unsubscribe'")
			else:
				message.reply("You're already subscribed to MemeAdviser! If you want to unsubscribe, reply with 'Unsubscribe'")

	# Mark all messages as read
	reddit.inbox.mark_read(unread_messages)

if __name__ == "__main__":
    main(True)
