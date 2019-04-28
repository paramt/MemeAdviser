class Thresholds:
    submission = 800
    comment = 1000
    pm = 1000


class Messages:
    comment = '''I **strongly advise** investing! This meme hit #1 on [hot](https://www.reddit.com/r/memeeconomy/hot/) within **{min}**, at **{upvotes}** upvotes. If you invest now, you'll break even at **{break_even}** upvotes.

    [Click here](https://www.param.me/meme/calculator/break-even) to calculate the current break-even point. [Click here](https://www.reddit.com/message/compose?to=MemeAdviser&subject=Subscribe&message=Subscribe) to subscribe to daily market updates.
    
    *****
    
    ^(Beep boop, I'm a bot | [Contact me](mailto://bot@param.me))
    '''

    submission = "This meme just hit #1 on MemeEconomy with only {upvotes} upvotes! Invest now and break even at {break_even} upvotes"

    pm = '''[This meme](https://reddit.com{link}) just hit #1 on MemeEconomy with only {upvotes} upvotes! Invest now and break even at {break_even} upvotes

    ***
    
    ^(You're recieving this message because you've subscribed to this bot. To unsubscribe, reply 'Unsubscribe')
    '''
