# MemeAdviser [<img height=44 src=docs/logo.png align=left>](https://www.param.me/MemeAdviser)
[![Build Status](https://travis-ci.org/paramt/MemeAdviser.svg?branch=master)](https://travis-ci.org/paramt/MemeAdviser)
[![Codecov](https://codecov.io/gh/paramt/memeadviser/branch/master/graph/badge.svg)](https://codecov.io/gh/paramt/MemeAdviser)
[![Dependencies Status](https://requires.io/github/paramt/MemeAdviser/requirements.svg?branch=master)](https://requires.io/github/paramt/MemeAdviser/requirements/?branch=master) <br>
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://github.com/paramt/MemeAdviser/blob/master/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/paramt/memeadviser/badge)](https://www.codefactor.io/repository/github/paramt/memeadviser)
[![Uptime](https://img.shields.io/uptimerobot/ratio/m782558720-9763f20f7351b4f41c81a7d6.svg?style=flat)](https://status.param.me/782558720)
[![Update Status](https://img.shields.io/endpoint.svg?url=https://thakkaha.dev.fast.sheridanc.on.ca/pme/meme/status/&style=flat)](https://github.com/MemeInvestor/memeinvestor_bot/blob/master/src/formula.py)

**MemeAdviser** is a reddit bot that analyzes the market at [r/MemeEconomy](https://www.reddit.com/r/MemeEconomy) and gives insightful information on investments.

## Features
#### Logs the front page
As soon as a meme hits #1 on [the front page](https://www.reddit.com/r/MemeEconomy/hot), the bot records the time it took and the amount of upvotes with which it reached there. Everything it's collected and recorded can be found [on the /r/MemeAdviser wiki](https://www.reddit.com/r/MemeAdviser/wiki). Gathering this data lets us gain better insight on front page patterns and lets us fine-tune the bot.

#### Finds investment opportunities
If the meme has a low number of upvotes at the time, the bot [comments on the meme](https://www.reddit.com/u/MemeAdviser/comments) and provides the break-even point for any investments made during that time. Additionally, it may post a link to [r/InsiderMemeTrading](https://www.reddit.com/r/InsiderMemeTrading).

#### Sends investment opportunities right to your PMs
The bot also lets users subscribe to it. When it finds a promising meme, it messages the link to everyone that's subscribed. It also provides a more in-depth analysis of the meme. Redditors can subscribe to the bot by sending a private message to [u/MemeAdviser](https://reddit.com/u/MemeAdviser) with the text "Subscribe" as the subject or body.

## Development
Just remember to create a new issue before working on a PR

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

## Production
The server executes `run.sh` every minute using **Python 3.6.7** and generates an internal log file. The log is uploaded online every 5 minutes and can be found here:

- [Online](https://www.param.me/MemeAdviser/log)
- [Raw](https://raw.githubusercontent.com/wiki/paramt/MemeAdviser/memeadviser.log)
