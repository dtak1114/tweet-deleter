# About

sets up AWS event + lambda function to periodically clean up your tweets posted before specified period.

# Prerequisites

- you have an AWS account and have done setup successfully with `aws configure`.
- you have your Twitter OAuth credential suites from [here](https://developer.twitter.com/en/portal/dashboard).
  - you will need to issue these 4 key/secrets to issue requests to Twitter.
    1. consumer key (`TW_CONSUMER_KEY`)
    2. consumer secret (`TW_CONSUMER_SECRET`)
    3. access token key (`TW_ACCESS_TOKEN_KEY`)
    4. access token secret (`TW_ACCESS_TOKEN_SECRET`)

# Deploy

1. install chalice dependency.

```sh
pip install -r requirements-dev.txt
```

2. replace credentials in `app.py`. 

3. deploy.

```sh
chalice deploy
```

# Configuration & Limitation

- Due to Twitter's [rate limit](https://developer.twitter.com/ja/docs/twitter-api/rate-limits), it removes upto `50 tweets/15min` == `200 tweets/1hour`. Just hold on tight..
- By default, tweets posted before 6 month from the moment of execution will be the target of clean up.
 - you can tweak by editing `app.py#REMOVE_BEFORE` if you'd like.