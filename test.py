import tweepy
import openai
import json
import time
# import pandas as pd
import re

# calling keys, secrets, tokens from config
from config import *
# openai.api_key = openai_key


# #Setting credentials to access Twitter API and scope for bookmark
# auth = tweepy.OAuth2UserHandler(
#     scope=["bookmark.read", "bookmark.write", "tweet.read", "users.read"],
#     redirect_uri = 'https://127.0.0.1:6006/callback', client_id=client_ID, client_secret=client_secret
#     )
# # auth.set_access_token(access_token, access_token_secret)

# print(auth.get_authorization_url())



# verifier = "https://oauth.pstmn.io/v1/browser-callback"
# access_token = auth.fetch_token(verifier)

# print(f"\naccess-token-pkce={access_token['access_token']}")


# access_token_pkce = access_token

# client = tweepy.Client(access_token)

# some_tweet = "1536895050176667649"
# # add tweet to bookmarks
# response = client.bookmark(tweet_id=some_tweet )
# print(f"Tweet {some_tweet} bookmarked: {response.data['bookmarked']}")


# print('zoo wee mama')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    if '@bookmark_io' in mention.text:
        keyword = re.findall(r'(?<=@bookmark_io ).+', mention.text)[0]
        bookmarks = api.bookmarks()
        tweets = []
        
        for bookmark in bookmarks:
            tweet = bookmark.tweet
            if keyword in tweet.text:
                tweets.append(tweet.text)
                user = mention.user
                message = "Here are the tweets I found matching your query:\n\n"
                message += "\n\n".join(tweets)
                api.send_direct_message(user.id, message)
            print(message)
# print(mentions)