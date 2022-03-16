# A script that gets the daily percentage change in price of a specified stock. 
# sends sms alerts when a specified price is reached
# Also sends accompanying relevant news gotten from newsapi
import math
from twilio.rest import Client
import requests

# twilio authentication
account_sid = "Your twilio account sid"
auth_token = 'Your twilio auth token'
client = Client(account_sid, auth_token)

# constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# get stock prices
ALPHA_VINTAGE_API = "Your alpha vintage API key"
analysis_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VINTAGE_API,
    "pageSize": 5

}
analysis_response = requests.get(url="https://www.alphavantage.co/query", params=analysis_parameters)
analysis_response.raise_for_status()
analysis = analysis_response.json()
daily_analysis = analysis["Time Series (Daily)"]

new_dict = [v for (k, v) in daily_analysis.items()]
y_day_open = float(new_dict[0]['1. open'])
db_yday_close = float(new_dict[1]['4. close'])


def calculate_percent(open, close):
    """calculates the percentage change of the opening and closing stock prices of the current day and previous day"""
    difference = open - close
    percent_diff = math.floor((difference / close) * 100)

    return percent_diff


percent = ""
percent_change = (calculate_percent(y_day_open, db_yday_close))
abs_percent = abs(percent_change)
if percent_change > 0:
    percent = f"TSLA: {abs_percent}%🔺 \n"
else:
    percent = f" TSLA: {abs_percent}%🔻 \n"

if abs_percent > 2:
    # get corresponding news
    NEWS_API = "Your news API key"
    NEWS_URL = "https://newsapi.org/v2/everything"
    news_parameters = {
        "apiKey": NEWS_API,
        "q": "tesla",

    }

    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    print(news_response.status_code)
    news = news_response.json()
    articles = news["articles"]
    main_news = articles[:3]
    alert = [
        f"Headline: {article['title']} \nBrief: {(article['description'])} \nLink: {(article['url'])} \n\n"
        for article in main_news]

    '''news_1 = f"Headline: {main_news[0]['title']} \nBrief: {(main_news[0]['description'])} \nLink: {(main_news[0]['url'])} \n\n"
    news_2 = f"Headline: {main_news[1]['title']} \nBrief: {(main_news[1]['description'])} \nLink: {(main_news[1]['url'])} \n\n"
    news_3 = f"Headline: {main_news[2]['title']} \nBrief: {(main_news[2]['description'])} \nLink: {(main_news[2]['url'])}"'''

    # SMS Alert

    # alert_format = percent + news_1 + news_2 + news_3
    for article in alert:
        print(article)

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
        to='Recipient phone number',
        body= article,
        from_='Your twilio number'
    )
