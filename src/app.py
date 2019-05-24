import logging
import os
import re
import time as t
import praw

import src.algorithm as algorithm
import src.constants as constants

# Configure logger
def setup_logger(logfile):
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(levelname)-8s %(asctime)s: %(message)s")
	file_handler = logging.FileHandler(logfile)
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
	logger.propagate = False

	logging.basicConfig(filename = logfile,
						level = logging.INFO,
						format = "%(levelname)-8s %(asctime)s: %(message)s")

	return logger

def login(usePreset, logger):
	try:
		if(usePreset):
			reddit = praw.Reddit('MemeAdviser')
		else:
			reddit = praw.Reddit(client_id=os.environ['CLIENT_ID'],
								client_secret=os.environ['CLIENT_SECRET'],
								user_agent=os.environ['USER_AGENT'],
								username=os.environ['USERNAME'],
								password=os.environ['PASSWORD'])
	except Exception as e:
		logger.critical("An error occured while attempting to log in: {} Exiting program".format(str(e)))
		exit()
	else:
		return reddit

def find_top_submission(reddit):
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

	return submission, time

def update_subscriptions(reddit, subscribed, logger):
	def update_file():
		with open("subscribed.txt", "w") as f:
			f.write("\n".join(subscribed) + "\n")

	unread_messages = []

	# Go through each unread message
	for message in reddit.inbox.unread():
		unread_messages.append(message)

		# Check for new unsubscriptions
		if re.search("unsubscribe", message.body, re.IGNORECASE) or re.search("unsubscribe", message.subject, re.IGNORECASE):
			if message.author.name in subscribed:
				subscribed.remove(message.author.name)
				update_file()
				message.reply("You've unsubscribed from MemeAdviser. To subscribe, reply with 'Subscribe'")
				logger.info("Removed {} from subscribed.txt".format(message.author.name))

			else:
				message.reply("You aren't subscribed to MemeAdviser! If you want to subscribe, reply with 'Subscribe'")

		# Check for new subscriptions
		elif re.search("subscribe", message.body, re.IGNORECASE) or re.search("subscribe", message.subject, re.IGNORECASE):
			if message.author.name not in subscribed:
				subscribed.append(message.author.name)
				update_file()
				message.reply("You've subscribed to MemeAdviser! To unsubscribe, reply with 'Unsubscribe'")
				logger.info("Added {} to subscribed.txt".format(message.author.name))

			else:
				message.reply("You're already subscribed to MemeAdviser! If you want to unsubscribe, reply with 'Unsubscribe'")

	# Mark all messages as read
	reddit.inbox.mark_read(unread_messages)

def main(usePreset: bool, thresholds=constants.Thresholds, logfile=constants.LOGFILE):
	logger = setup_logger(logfile)
	reddit = login(usePreset, logger)

	submission, time = find_top_submission(reddit)

	with open("replied.txt", "r") as f:
		replied = f.read().splitlines()

	with open("subscribed.txt", "r") as f:
		subscribed = f.read().splitlines()

	if submission.id not in replied:
		logger.info("New submission found ({})".format(submission.id))

		try:
			# Update replied.txt
			replied.append(submission.id)
			with open("replied.txt", "w") as f:
				for post_id in replied:
					f.write(post_id + "\n")

		except IOError as e:
			logger.critical("An error occured while updating replied.txt: {} Exiting program".format(str(e)))
			exit()

		else:
			logger.info("Updated replied.txt")

		try:
			# Post to r/InsiderMemeTrading
			if submission.score < thresholds.submission:
				reddit.subreddit("InsiderMemeTrading").submit(title=constants.Messages.submission.format(upvotes=submission.score, break_even=algorithm.break_even(submission.score)), url="https://reddit.com" + submission.permalink)
				logger.info("Posted link to submission on r/InsiderMemeTrading")

			# Send PM to subscribers
			if submission.score < thresholds.pm:
				logger.debug("Attempting to send PMs to {} subscribers".format(len(subscribed)))
				for user in subscribed:
					reddit.redditor(user).message("MemeEconomy Update", constants.Messages.pm.format(link=submission.permalink, upvotes=submission.score, break_even=algorithm.break_even(submission.score)))
				logger.info("Sent PMs to {} subscribers".format(len(subscribed)))

			# Comment on r/MemeEconomy post
			if submission.score < thresholds.comment:
				submission.reply(constants.Messages.comment.format(upvotes=str(submission.score), time=time, break_even=algorithm.break_even(submission.score)))
				logger.info("Commented on r/MemeEconomy submission")

		except Exception as e:
			logger.critical("An error occured while replying to the submission: {} Exiting program".format(str(e)))
			exit()

	update_subscriptions(reddit, subscribed, logger)

if __name__ == "__main__":
    main(True)
