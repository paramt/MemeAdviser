# MemeAdviser <img height=44 src=docs/logo.png align=left>
[![Uptime](https://img.shields.io/uptimerobot/ratio/m782558720-9763f20f7351b4f41c81a7d6.svg?style=for-the-badge)](https://status.param.me/782558720)
![Update Status](https://img.shields.io/endpoint.svg?url=https://thakkaha.dev.fast.sheridanc.on.ca/pme/meme/status/&style=for-the-badge)

**MemeAdviser** is a reddit bot that analyzes the market at [r/MemeEconomy](https://www.reddit.com/r/MemeEconomy) and gives insightful information.

### Features
#### Logs the front page
As soon as a post hits #1 on [the front page](https://www.reddit.com/r/MemeEconomy/hot), it records the time it took and the amount of upvotes with which it reached there. Everything it's collected and recorded can be found [here](https://www.reddit.com/u/MemeAdviser/comments).

#### Posts promising memes to r/InsiderMemeTrading
If the post has a low number of upvotes at the time, it posts the link to [r/InsiderMemeTrading](https://www.reddit.com/r/InsiderMemeTrading) and provides the break-even point for any investments made during that time. These can be found [here](https://www.reddit.com/u/MemeAdviser/posts).

#### Subscriptions
The bot lets users subscribe to it. When it finds a promising meme, it messages the link to everyone that's subscribed. It also provides a more in-depth analysis of the meme. Redditors can subscribe to the bot by sending a private message to [u/MemeAdviser](https://reddit.com/u/MemeAdviser) with the text "Subscribe" as the subject or body.

### TODO
 - [x] Allow Redditors to subscribe to the bot to receive regular updates on the market
 - [x] ~~Calculate the current break-even point of an investment when summoned with ```!breakeven```~~
 - [ ] Monitor more of the front page (like top 5 or top 10 on hot)
 - [ ] ~~Allow users to ```!watch``` a post, which will send updates to the user for the next 4 hours~~
 - [ ] Automatically update the formula the [official formula](https://github.com/MemeInvestor/memeinvestor_bot/blob/master/src/formula.py)

 \*commands will not be added because it creates too much spam
