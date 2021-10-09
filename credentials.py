import tweepy

access_token = "1012873487763927040-XvhSTE4wrBXNxPPEqB7USvguKgWeJS"
access_secret = "JyNtmERR1J79r2qtOl3wPBbIiLiG7pHmn3hrO4taYLFMq"

bearer_token = "AAAAAAAAAAAAAAAAAAAAAAf0EwEAAAAAVEp9Am5LDcn8sq%2BKDPiGRCICE68%3DoEMgv2VN7alC7ojd68VfBltZRx7hTdhUBim07BnVpHRtnT9nQi"
consumer_key = "ECL4jj39YeN3jk5GFrIHDvpLY"
consumer_secret = "N3spDwQnQI1SyibGmXGDyCsQqHzPsvSVSCHn5nz7be6YLPlCUi"


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")