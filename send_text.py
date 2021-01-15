from src.smtp_text import smtp_text
from src.twitter_api import twitter_api
import config
from config import *
import time
import importlib

text_smtp = smtp_text(GMAIL_EMAIL, GMAIL_PASSWORD)
twitter_account = twitter_api(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweet_text, time_in_seconds = twitter_account.get_latest_tweet()

while True:
    twitter_account.reconnect()
    if twitter_account.set_tweet_time_if_latest(time_in_seconds):
        importlib.reload(config)
        from config import PHONE_NUMBERS

        for phone_number in PHONE_NUMBERS:
            text_smtp.send_message(phone_number, tweet_text)
            print(f"Successfully sent updated tweet to {phone_number} - {PHONE_NUMBERS[phone_number]}")

    # Wait 15 minutes and then recheck
    time.sleep(900) 