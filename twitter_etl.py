import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():


    access_key = "XXXXXXXXXXX"  #api key
    access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  #api key secret
    consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  #acces token
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"    #acees token secret
     


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   #refer tweepy documentation
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)  #create ojcet for api pass varibale like keys 
    tweets = api.user_timeline(screen_name='@iamsrk', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,    
                            #for retweets variable
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
   


    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv('s3://akshaytweet/srk.csv') 
    #after creating bucket just copy bucket name and give file you want to save data
    #bucket  akshaytweet
    #file srk

 
