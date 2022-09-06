from chalice import Chalice, Rate
import tweepy
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

# by default, tweets before 6 months from now are removed.
REMOVE_BEFORE = datetime.now() -relativedelta(months=6)

app = Chalice(app_name='tweet-deleter')

client = tweepy.Client(
    consumer_key=os.environ.get('TW_CONSUMER_KEY'),
    consumer_secret=os.environ.get('TW_CONSUMER_SECRET'),
    access_token=os.environ.get('TW_ACCESS_TOKEN_KEY'),
    access_token_secret=os.environ.get('TW_ACCESS_TOKEN_SECRET'),
    )


def get_my_user_id():
    u = client.get_me()
    return u.data['id']

def delete_tweets_before(myid, dt, next_token=None):
    res = client.get_users_tweets(
        myid,
        pagination_token=next_token,
        user_auth=True,
        end_time=dt,
        max_results=50)
    count = 0
    if res.data is not None:
        for t in res.data:
            
            print(t)
            count += 1
    return count

# Automatically runs every day
@app.schedule(Rate(15, unit=Rate.MINUTES))
def delete_tweets(event):
    myid = get_my_user_id()
    deleted = delete_tweets_before(myid,REMOVE_BEFORE)
    return deleted

if __name__ == '__main__':
    delete_tweets()