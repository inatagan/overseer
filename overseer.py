from dotenv import load_dotenv
import os
import praw
from datetime import datetime



def main():
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.environ.get('my_client_id'),
        client_secret=os.environ.get('my_client_secret'),
        user_agent=os.environ.get('my_user_agent'),
        username=os.environ.get('my_username'),
        password=os.environ.get('my_password'),
    )


    sub=os.environ.get('my_subreddit')
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.stream.submissions(skip_existing=True):
        user = submission.author
        user_submissions = get_total_submissions(reddit, submission.author)
        user_comments = get_total_comments(reddit, submission.author)
        account_age = get_age(user.created_utc)
        bot_reply = submission.reply(body=REPLY_TEMPLATE.format(user.name, submission.author_flair_text, user_submissions, user_comments, account_age, sub, submission.url))
        bot_reply.mod.distinguish(how="yes", sticky=True)
        bot_reply.mod.lock()


def get_total_comments(reddit, user):
    total_comments = 0
    for comment in reddit.redditor(user.name).comments.new(limit=None):
        total_comments += 1
    return total_comments


def get_total_submissions(reddit, user):
    total_submissions = 0
    for submission in reddit.redditor(user.name).submissions.top(limit=None):
        total_submissions += 1
    return total_submissions


def get_age(user_created_utc):
    age = datetime.now() - datetime.fromtimestamp(user_created_utc)
    seconds_in_year = 365.25*24*60*60
    seconds_in_month = 30*24*60*60
    if age.total_seconds() > seconds_in_year:
        return f"{int(age.total_seconds() / seconds_in_year)} years"
    elif age.total_seconds() > seconds_in_month:
        return f"{int(age.total_seconds() / seconds_in_month)} months"
    else:
        return f"{age.days} days"



REPLY_TEMPLATE = """**Trader** | {}
:-:|:-:
**Rank** | {}
**Total Submissions** | {}+
**Total Comments** | {}+
**Account age** | {}
**Report this trade** | [report](https://reddit.com/message/compose?to=/r/{}&subject=Trade%20Report&message=%23%23%23%20My%20info%0AMy%20reddit%20username%3A%0A%0AMy%20Account%20%5BPSN%20%7C%20GAMERTAG%20%7C%20STEAM%20ID%5D%3A%0A%0A%23%23%23%20Want%20to%20report%20the%20following%20user%0A%0AReddit%20username%3A%0A%0AAccount%20%5BPSN%20%7C%20GAMERTAG%20%7C%20STEAM%20ID%5D%3A%0A%0A%23%23%23%20What%20happened%3F%0A%5BAdd%20description%20here%5D%0A%0A%23%23%23%20Evidences%0A%5BAdd%20here%20any%20screenshots%20or%20videos%20of%20the%20occurrence%20that%20you%20have%2C%20PS%3A%20you%20must%20upload%20the%20screenshots%20or%20video%20to%20a%20hosting%20service%20and%20them%20copy%20and%20paste%20the%20link%20here.%5D%0A%0A%0A%5BDO%20NOT%20CHANGE%20THIS%20LINK%5D%0Apermalink%3A{})
"""




if __name__ == '__main__':
    main()

