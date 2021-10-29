import tweepy
import requests
import time
import csv

# these should be read from env variables
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Download all the tweets of a twitter user
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth) 
    alltweets = []   
    new_tweets = api.user_timeline(screen_name = screen_name,count=200) 
    alltweets.extend(new_tweets) 
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1 
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}") 
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) 
        alltweets.extend(new_tweets) 
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1 
        print(f"...{len(alltweets)} tweets downloaded so far") 
    outtweets = [tweet.text for tweet in alltweets] 
    with open(f'new_{screen_name}_tweets.txt', 'w') as f:
        text = ' '.join(outtweets)
        f.write(text)
    pass

# read the data on file to a string
def read_user_tweets(username):
    with open(f'new_{username}_tweets.txt', 'r') as f:
        return ' '.join(f.readlines())

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("J_tsar")
