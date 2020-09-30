import tweepy
import pandas as pd

class tweet_location:
    """
    Obtains tweet location by passing tweet ids through the parser.
    """

    def __init__(self, id):
        self.id = id

    def get_location(id):
        try:
            tweet_status = api.get_status(id)
            tweet_location = tweet_status.user.location
            tweet_data = [id, tweet_location]
            return(tweet_data)
        except:
            print("Tweet ID not found")
