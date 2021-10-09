import tweepy
from flask import Flask

import replyTweet

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

def job():
 replyTweet.respondToTweet("tweet_ID.txt")
 print("Success")

scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=60)
scheduler.start()

application = Flask(__name__)

@application.route("/")
def index():
 return "Follow @Kang_galonnn"

atexit.register(lambda: scheduler.shutdown())

if __name__=="__main__":
 application.run(port=5000, debug=True)
