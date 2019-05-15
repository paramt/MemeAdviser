from src import app
from src.constants import Thresholds

test = Thresholds()
test.comment, test.submission, test.pm = (0, 0, 0)

def test_app():
	with open("replied.txt", "w+"), open("subscribed.txt", "w+"):
		pass

	app.main(False, test)
