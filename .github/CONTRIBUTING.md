# Contributing
Before you start working on a PR, please create an issue to open up discussion.

## Development

#### 1. Clone the repo
 - `git clone https://github.com/paramt/MemeAdviser.git`
 - `cd MemeAdviser`

#### 2. Install dependencies
`pip install -r requirements.txt`

#### 3. Configure PRAW
- Create a new app on Reddit
    * [Follow this link](https://www.reddit.com/prefs/apps/)
    * Click **create new app**
    * Choose **personal use script**
    * Add a name and description
    * Click **create app** and copy the ID and secret
- Export the following environment variables:
```ini
client_id=[YOUR APP ID]
client_secret=[YOUR APP SECRET]
username=[YOUR REDDIT USERNAME]
password=[YOUR REDDIT PASSWORD]
user_agent=MemeAdviser Dev 1.0
```

#### 4. Run tests
Run `pytest -v` to run the bot without replying to submissions on reddit.

## Environment
The server executes `python -m src.app` every minute using Python 3.6.7 <br>
To run `python -m src.app` locally, you'll need to create a [`praw.ini` configuration](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#defining-additional-sites) in `src/`
