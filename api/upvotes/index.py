import os
import praw
from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_upvotes(path):
	reddit = praw.Reddit(client_id=os.environ["CLIENT_ID"],
						 client_secret=os.environ["CLIENT_SECRET"],
						 user_agent=os.environ["USER_AGENT"],
						 username=os.environ["USERNAME"],
						 password=os.environ["PASSWORD"])
	submission_id = request.args["id"]
	submission = reddit.submission(id=submission_id)
	upvotes = submission.score
	return Response(f"{{'status': 201, 'submission': {submission_id}, 'upvotes': {upvotes} }}", mimetype='application/json')
