import tweepy

#replace this with your twitter keys
consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

#import my keys 
try:
	from keys import consumer_key, consumer_secret, access_token, access_token_secret
except Exception as e:
	print ("Import Failed")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = {}

for tweet in tweepy.Cursor(api.search,q="#MeToo", count=100, lang="en", since="2018-03-21").items():
	date = tweet.created_at.strftime("%d-%m-%Y %H")
	
	try:
		retrieve_score = tweets[date]

	except Exception as e:
		tweets[date] = {'retweets': 0, 'tweet': 0, 'likes': 0}
		retrieve_score = tweets[date]

	#retweets of your tweet
	retrieve_score['retweets'] += tweet.retweet_count
	#add likes count
	retrieve_score['likes'] += tweet.favorite_count

	#add's one if it's also a retweet
	if tweet.retweeted:
		retrieve_score['retweets'] += 1

	else: #if unique/edited/new adds to tweet
		retrieve_score['tweet'] += 1


