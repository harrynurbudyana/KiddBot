FROM python3.9

COPY replyTweet.py /bots
COPY main.py /bots
COPY credentials.py /bots

WORKDIR /bots
CMD ["python3", "main.py"]


