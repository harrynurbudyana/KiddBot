import tweepy
import json
import requests
import logging

import img_src
import time

import credentials

consumer_key = credentials.consumer_key
consumer_secret_key = credentials.consumer_secret
access_token = credentials.access_token
access_secret = credentials.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

def get_meme():
 url= "https://ronreiter-meme-generator.p.rapidapi.com/meme"
 headers = {
  'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
    'x-rapidapi-key': "c9617a9429msh1e1fcceb3680a3cp11d77cjsn63a32f5ea8c0"
 }
 try:
  response = requests.get(url, headers=headers)
 except:
  logger.info("Error While Calling API...")
 
 res = json.loads(response.text)
 print(res)
 return res

def get_quote():
 url = "https://api.quotable.io/random"

 try: 
  response = requests.get(url)
 except:
  logger.info("Error While Calling API...")

 res = json.loads(response.text)
 print(res)
 return res['content'] + "-" + res['author']

def get_last_tweet(file):
 f = open(file, 'r')
 lastId = int(f.read().strip())
 f.close()
 return lastId

def put_last_tweet(file, Id):
 f = open(file, 'w')
 f.write(str(Id))
 f.close()
 logger.info("Updated the file to the latest tweet Id")
 return

def respondToTweet(file):
 last_id = get_last_tweet(file)
 mentions = api.mentions_timeline(last_id, tweet_mode='extended')
 if len(mentions) == 0:
  return

 for mention in reversed(mentions):
  new_id = mention.id
  if 'quote' in mention.full_text.lower():
   try :
    tweet = get_quote()
    img_src.get_wallpaper(tweet)
    media = api.media_upload()
    logger.info("liking and  replying to tweet")

    api.create_favorite(mention.id)
    api.update_status('@' + mention.user.screen_name + "Here's your Quote", mention.id,
                       media_ids=[media.media_id])
   except :
    logger.info("Already replied to {}".format(mention.id))
  if 'test' in mention.full_text.lower():
   try :
    tweet = "Bot gua nih bos, senggol dong!"
    api.update_status(tweet)

   except : 
    logger.info("Already replied to {}".format(mention.id))

 put_last_tweet(file, new_id)

def main():
 respondToTweet()


if __name__=="__main__":
 main()

    




