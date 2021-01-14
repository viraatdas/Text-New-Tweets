from src.smtp_text import smtp_text
from src.twitter_api import twitter_api
from config import *
import time
import importlib

phone_numbers = []
with open('phone_numbers.txt') as f:
    phone_numbers = f.read().splitlines()

text_smtp = smtp_text(GMAIL_EMAIL, GMAIL_PASSWORD)
twitter_account = twitter_api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

a = twitter_account.get_api()
tweet_text, time_in_seconds = twitter_account.get_latest_tweet()


while True:
    # if twitter_account.set_tweet_time_if_latest(time_in_seconds):
    importlib.reload(config)
    from config import PHONE_NUMBERS

    for phone_number in PHONE_NUMBERS:
        text_smtp.send_message(phone_number, tweet_text)
        print(f"Successfully sent updated tweet to {phone_number}")
    time.sleep(10)