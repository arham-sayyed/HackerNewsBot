import tweepy
import io
from api_secrets import twitter_secrets

api_key = twitter_secrets['api_key']
api_secret = twitter_secrets['api_secret']
bearer_token = twitter_secrets['bearer_token']
access_token = twitter_secrets['access_token']
access_token_secret = twitter_secrets['access_token_secret']


def tweet_img_with_text(tweet_text, image_path, filename):
    try: 
        client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api = tweepy.API(auth)

        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        media = api.media_upload(filename, file=io.BytesIO(image_data))
        media_id = media.media_id_string
        
        client.create_tweet(text= tweet_text, media_ids=[media_id])
        return True
    except Exception as e:
        print(f"ERROR while 'tweet_img_with_text': {e}")
        return None
    
