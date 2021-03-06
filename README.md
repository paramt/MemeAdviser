# MemeAdviser [<img height=44 src=docs/logo.png align=left>](https://www.param.me/MemeAdviser)

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-blue.svg)](https://github.com/paramt/MemeAdviser/blob/master/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/paramt/memeadviser/badge)](https://www.codefactor.io/repository/github/paramt/memeadviser)

**MemeAdviser** is a reddit bot that analyzes the market at [r/MemeEconomy](https://www.reddit.com/r/MemeEconomy) and gives insightful information on investments.

## Features
#### Logs the front page
As soon as a meme hits #1 on [the front page](https://www.reddit.com/r/MemeEconomy/hot), the bot records the time it took and the amount of upvotes with which it reached there. Everything it's collected and recorded can be found [on the /r/MemeAdviser wiki](https://www.reddit.com/r/MemeAdviser/wiki). Gathering this data lets us gain better insight on front page patterns and lets us fine-tune the bot.

#### Finds investment opportunities
If the meme has a low number of upvotes at the time, the bot [comments on the meme](https://www.reddit.com/u/MemeAdviser/comments) and provides the break-even point for any investments made during that time. 

#### Sends investment opportunities right to your PMs
The bot also lets users subscribe to it. When it finds a promising meme, it messages the link to everyone that's subscribed. It also provides a more in-depth analysis of the meme. Redditors can subscribe to the bot by sending a private message to [u/MemeAdviser](https://reddit.com/u/MemeAdviser) with the text "Subscribe" as the subject or body.


## Development
This repository has been archived and no new PRs will be merged.

### Production Environment
- Ubuntu 18.04 LTS
- Python 3.6.7

### Log
The logfile is pushed online every 5 minutes

- [Web](https://www.param.me/MemeAdviser/log)
- [Raw](https://raw.githubusercontent.com/wiki/paramt/MemeAdviser/memeadviser.log)

## License
This project is licensed under the [Mozilla Public License 2.0](LICENSE)
