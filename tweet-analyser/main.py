import tweepy
from textblob import TextBlob

# twitter authorization keys
consumer_key = 'QT21yRpLeoSfoXoikEiFnJyBh'
consumer_secret = 'f7v908zedgcl9aGBr0FmX4cn34XZTESGSiP1Q6TbDkdUK6Kwt5'
access_token = '362505559-0JHYOj6LqftxR0Njbs9ui7VUVFtXcbA5OWunmhAT'
access_token_secret = '29NAEzwIm3VHUSZQiNadWRmZvIEM1iM3YluFzqLwHMLY4'

# create auth using tweepy's oauth commands
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialize api
api = tweepy.API(auth)

# search for tweets
public_tweets = api.search('Trump')

#print tweets and their sentiment value
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)