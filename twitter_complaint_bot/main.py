from internet_speed_bot import InternetSpeedTwitterBot
PROMISED_DOWN = 2
PROMISED_UP = 2


twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
if twitter_bot.up < PROMISED_UP or twitter_bot.down < PROMISED_DOWN:
    upload = twitter_bot.up
    download = twitter_bot.down
    twitter_bot.tweet_at_provider(upload=upload, download=download)
