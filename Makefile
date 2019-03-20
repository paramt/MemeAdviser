bot:
	python3 app.py
.PHONY: bot

lint:
	python3 -m flake8 --ignore=E501,E722 *.py
.PHONY: lint
