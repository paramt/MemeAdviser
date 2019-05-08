# MemeAdviser <img height=44 src=docs/logo.png align=left>
[![CodeFactor](https://www.codefactor.io/repository/github/paramt/memeadviser/badge)](https://www.codefactor.io/repository/github/paramt/memeadviser)
[![Uptime](https://img.shields.io/uptimerobot/ratio/m782558720-9763f20f7351b4f41c81a7d6.svg?style=flat)](https://status.param.me/782558720)
[![Update Status](https://img.shields.io/endpoint.svg?url=https://thakkaha.dev.fast.sheridanc.on.ca/pme/meme/status/&style=flat)](https://github.com/MemeInvestor/memeinvestor_bot/blob/master/src/formula.py)

**MemeAdviser** is a reddit bot that analyzes the market at [r/MemeEconomy](https://www.reddit.com/r/MemeEconomy) and gives insightful information.

### Features
#### Logs the front page
As soon as a post hits #1 on [the front page](https://www.reddit.com/r/MemeEconomy/hot), it records the time it took and the amount of upvotes with which it reached there. Everything it's collected and recorded can be found [here](https://www.reddit.com/u/MemeAdviser/comments).

#### Posts promising memes to r/InsiderMemeTrading
If the post has a low number of upvotes at the time, it posts the link to [r/InsiderMemeTrading](https://www.reddit.com/r/InsiderMemeTrading) and provides the break-even point for any investments made during that time. These can be found [here](https://www.reddit.com/u/MemeAdviser/posts).

#### Subscriptions
The bot lets users subscribe to it. When it finds a promising meme, it messages the link to everyone that's subscribed. It also provides a more in-depth analysis of the meme. Redditors can subscribe to the bot by sending a private message to [u/MemeAdviser](https://reddit.com/u/MemeAdviser) with the text "Subscribe" as the subject or body.

### Development
Create a new issue before working on a PR to prevent wasted effort

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
- Create a new file named `praw.ini`
- Make a new configuration that looks like this
```
[MemeAdviser]
client_id=[YOUR APP'S ID]
client_secret=[YOUR APP'S SECRET]
username=[YOUR REDDIT USERNAME]
password=[YOUR REDDIT PASSWORD]
user_agent=MemeAdviser Dev 1.0
```
