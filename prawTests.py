import praw

reddit_bot = praw.Reddit(user_agent='RedditBot426 v0.1',
                  client_id='mXTCjODSk62Zeg',
                  client_secret='RUl-LK40XqBeOEa1-vIw54uVI2Q',
                  username='RedditBot426',
                  password='redditbot426')

print('Current user account logged into: ', end='')
print(reddit_bot.user.me())


# Set up appropriate subreddit and keywords for comment search
subreddit = input("Which subreddit would you like to monitor? >>")
keywords = input("Which keywords would you like to search for? >>")
bot_subreddit = reddit_bot.subreddit(subreddit)
sub_comments = bot_subreddit.stream.comments()

for comment in sub_comments:
    text = comment.body
    author = comment.author
    comment_subreddit = comment.subreddit
    if keywords.lower() in text.lower():
        # print("Repying to {}'s comment..". format(author))
        # comment.reply("Hatred leads to suffering, u/{}.". format(author))
        print("u/{} made a comment in r/{} containing your keywords.".format(author,comment_subreddit))

